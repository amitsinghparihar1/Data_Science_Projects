import os
import json
import pandas as pd
import traceback
from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.logger import logging
import streamlit as st
from dotenv import load_dotenv
from langchain.callbacks import get_openai_callback
from src.mcqgenerator.MCQgen import generate_evaluate_chain
import json

# loading json file
with open("C:\\Users\\amits\\Gen-AI-Projects\\McqGen\\Response.json", "r") as file:
    RESPONSE_JSON=json.load(file)
    
# creating a title for the app
st.title("MCQ Creator With Langchain")

# create a form using st.form
with st.form('user_inputs'):
    # File Upload
    uploaded_files=st.file_uploader('Upload A PDF or Text File')
    
    # Input Fields
    mcq_count=st.number_input('Number of MCQs', min_value=3, max_value=40)
    
    # subject
    subject=st.text_input('Insert Subject', max_chars=20)

    # quiz tone
    tone=st.text_input('Complexity level of Questions', max_chars=20, placeholder='simple')
    
    # Add button
    button=st.form_submit_button('Click Here to Create MCQs')
    
    if button and uploaded_files is not None and mcq_count and subject and tone:
        with st.spinner("loading..."):
            try:
                text=read_file(uploaded_files)
                # Count tokens and cost of API Call
                with get_openai_callback() as cb:
                   response = generate_evaluate_chain({
                       
                        "text": text,
                        "number": mcq_count,
                        "subject": subject,
                        "tone": tone,
                        "response_json": json.dumps(RESPONSE_JSON),
                        })
                    # st.write(response)
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error('An error occurred while processing. Please try again.'+ str(e))
            else:
                print(f"Total Tokens:{cb.total_tokens}")
                print(f"Prompt Tokens:{cb.prompt_tokens}")
                print(f"Completion Tokens:{cb.completion_tokens}")
                print(f"Total Cost:{cb.total_cost}")
                if isinstance(response, dict):
                    # Extract quiz data from response
                    quiz=response.get("quiz",None)
                    if quiz is not None:
                        table_data = get_table_data(quiz)  # Pass `quiz` as an argument
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index = df.index + 1
                            st.table(df)
                            # Display the review in a text box as well
                            st.text_area(label='review', value=response['review'])
                        else:
                            st.error('Error in the table data')
                else:
                    st.write(response)
    