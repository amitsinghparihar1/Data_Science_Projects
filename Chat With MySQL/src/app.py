from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
import streamlit as st

def init_database(user: str, password: str, host: str, port: str, database: str) -> SQLDatabase:
    db_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    return SQLDatabase.from_uri(db_uri)

def get_sql_chain(db):
    template = """
    You are a data analyst at a company. You are interacting with a user who is asking you questions about the company's database.
    Based on the table schema below, write a SQL query that would answer the user's question. Take the conversation history into account.

    <SCHEMA>{schema}</SCHEMA>

    Conversation History: {chat_history}

    Write only the SQL query and nothing else. Do not wrap the SQL query in any other text, not even backticks.

    For example:
    Question: which 3 artists have the most tracks?
    SQL Query: SELECT ArtistId, COUNT(*) as track_count FROM Track GROUP BY ArtistId ORDER BY track_count DESC LIMIT 3;
    Question: Name 10 artists
    SQL Query: SELECT Name FROM Artist LIMIT 10;

    Your turn:

    Question: {question}
    SQL Query:
    """

    prompt = ChatPromptTemplate.from_template(template)
    llm = ChatOpenAI(model="gpt-3.5-turbo")

    def get_schema(_):
        return db.get_table_info()

    return (
        RunnablePassthrough.assign(schema=get_schema)
        | prompt
        | llm
        | StrOutputParser()
    )

def get_response(user_query: str, db: SQLDatabase, chat_history: list):
    sql_chain = get_sql_chain(db)

    template = """
    You are a data analyst at a company. You are interacting with a user who is asking you questions about the company's database.
    Based on the table schema below, question, sql query, and sql response, write a natural language response.
    <SCHEMA>{schema}</SCHEMA>

    Conversation History: {chat_history}
    SQL Query: <SQL>{query}</SQL>
    User question: {question}
    SQL Response: {response}"""

    prompt = ChatPromptTemplate.from_template(template)
    llm = ChatOpenAI(model="gpt-3.5-turbo")

    chain = (
        RunnablePassthrough.assign(query=sql_chain).assign(
            schema=lambda _: db.get_table_info(),
            response=lambda vars: db.run(vars["query"]),
        )
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain.invoke({
        "question": user_query,
        "chat_history": chat_history,
    })

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hello! I am SQL Assistant. Ask me anything about your database")
    ]

load_dotenv()

st.set_page_config(page_title="Chat With MySQL", page_icon=":speech_balloons:")

st.title("Chat With MySQL")

with st.sidebar:
    st.subheader("Settings")
    st.write("This is a simple chat application using MySQL. Connect to the database and start chatting")

    st.text_input("Host", value="localhost", key='host')
    st.text_input("Port", value="3306", key='port')
    st.text_input("User", value="root", key='user')
    st.text_input("Password", type='password', value="admin", key='password')
    st.text_input("Database", value="smartphones", key='database')
    if st.button("Connect"):
        with st.spinner("Connecting to the database.."):
            db = init_database(
                st.session_state["user"],
                st.session_state["password"],
                st.session_state["host"],
                st.session_state["port"],
                st.session_state["database"]
            )
            st.session_state.db = db
            st.success("Connected to the database")

for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        st.markdown(f"**AI:** {message.content}")
    elif isinstance(message, HumanMessage):
        st.markdown(f"**You:** {message.content}")

user_query = st.text_input("Type a message...")
if user_query:
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    
    st.markdown(f"**You:** {user_query}")
    
    response = get_response(user_query, st.session_state.db, st.session_state.chat_history)
    st.markdown(f"**AI:** {response}")
    
    st.session_state.chat_history.append(AIMessage(content=response))


