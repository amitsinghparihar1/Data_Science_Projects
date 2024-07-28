import os
from dotenv import load_dotenv
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
from langchain.llms import GooglePalm
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX
from few_shots import few_shots
import streamlit as st

# Load environment variables
load_dotenv()


pinecone_api_key = os.environ.get("PINECONE_API_KEY")
DB_user = os.environ.get("DB_user")
DB_password = os.environ.get("DB_password")
DB_host = os.environ.get("DB_host")
DB_port = os.environ.get("DB_port")
DB_name = os.environ.get("DB_name")

# Configure Pinecone client
pc = Pinecone(api_key=pinecone_api_key)

# Define Pinecone index details
index_name = "test"
dimension = 384  # Dimension of the embeddings from the model

# Get a handle to the Pinecone index
index = pc.Index(index_name)

# Fetch the maximum value of Last_Session dynamically
def get_max_last_session(sql_db):
    query = "SELECT MAX(Last_Session) FROM execution_summarry"
    result = sql_db.run(query)
    max_last_session = result[0][0]
    return max_last_session

def get_few_shot_db_chain() -> SQLDatabaseChain:
    # Database connection details
    db_user = DB_user
    db_password = DB_password
    db_host = DB_host
    db_port = DB_port
    db_name = DB_name  

    # Initialize the database
    db = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    sql_db = SQLDatabase.from_uri(db)
    
    # Get the maximum value of Last_Session dynamically
    max_last_session = get_max_last_session(sql_db)

    # Initialize the language model
    llm = GooglePalm(google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0.1)
    
    # Convert few-shot examples to embeddings
    model_name = 'sentence-transformers/all-MiniLM-L6-v2'
    model = SentenceTransformer(model_name)
    to_vectorize = [" ".join(str(value) for value in example.values()) for example in few_shots]
    embeddings = model.encode(to_vectorize)

    
    # Prepare the embeddings for Pinecone upsert
    vectors_to_upsert = [
        (
            f"query_{i+1}",
            embedding.tolist(),
            {
                "Question": few_shots[i]["Question"],
                "SQLQuery": few_shots[i]["SQLQuery"],
                "SQLResult": str(few_shots[i]["SQLResult"]),
                "Answer": few_shots[i]["Answer"]
            }
        )
        for i, embedding in enumerate(embeddings)
    ]
    index.upsert(vectors=vectors_to_upsert, namespace="example-namespace2")

    # Define the example prompt template
    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )

    # Define the example selector using Pinecone query
    def example_selector(query_embedding, namespace="example-namespace2"):
        response = index.query(
            namespace=namespace,
            vector=query_embedding.tolist(),
            top_k=5,
            include_values=True,
            include_metadata=True  # Ensure metadata is included in the response
        )
        return response['matches']

    # Function to get the few-shot examples based on the input question
    def get_few_shot_examples(input_question):
        query_embedding = model.encode(input_question)
        matches = example_selector(query_embedding)
        return [
            {
                "Question": match["metadata"]["Question"],
                "SQLQuery": match["metadata"]["SQLQuery"],
                "SQLResult": match["metadata"]["SQLResult"],
                "Answer": match["metadata"]["Answer"],
            }
            for match in matches
        ]
        
    # Define the MySQL prompt
    mysql_prompt = f"""You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.
    Unless the user specifies in the question a specific number of examples to obtain, query for at most {{top_k}} results using the LIMIT clause as per MySQL. You can order the results to return the most informative data in the database.
    Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
    Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
    Pay attention to use CURDATE() function to get the current date, if the question involves "today".
    The value of the last session should be dynamically determined. Use the highest value of Last_Session available in the database, which is {max_last_session}.

    Use the following format:

    Question: Question here
    SQLQuery: Query to run with no pre-amble
    SQLResult: Result of the SQLQuery
    Answer: Final answer here

    No pre-amble.
    """

    # Example few-shot examples
    example_input = "Example input question to retrieve few-shot examples."
    few_shot_examples = get_few_shot_examples(example_input)

    few_shot_prompt = FewShotPromptTemplate(
        examples=few_shot_examples,
        example_prompt=example_prompt,
        prefix=mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "top_k"],  # These variables are used in the prefix and suffix
    )

    # Initialize the SQLDatabaseChain with the few-shot prompt
    chain = SQLDatabaseChain.from_llm(llm, sql_db, verbose=True, prompt=few_shot_prompt)
    
    return chain







