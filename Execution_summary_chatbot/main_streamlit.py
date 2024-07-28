import streamlit as st
from langchain_helper import get_few_shot_db_chain

# Initialize session state for storing conversation history and feedback
if 'conversation_history' not in st.session_state:
    st.session_state['conversation_history'] = []
if 'feedback' not in st.session_state:
    st.session_state['feedback'] = []

# Title and Header
st.title("💬 Execution Summary Chatbot")
st.subheader("Ask questions about execution summaries and get instant answers!")

# Custom CSS styling
st.markdown("""
    <style>
    body {
        font-family: 'Arial', sans-serif;
    }
    .main-header {
        color: #4B0082;
    }
    .chat-container {
        background-color: #f9f9f9;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        border: 1px solid #ddd;
    }
    .user-message, .bot-message {
        background-color: #ffffff;
        color: #333;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 5px;
    }
    .user-message {
        text-align: right;
    }
    .bot-message {
        text-align: left;
    }
    .text-input {
        background-color: #ffffff !important;
        color: #333;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #ddd;
        margin-bottom: 10px;
    }
    .text-input:focus {
        outline: none;
        border-color: #4B0082;
    }
    .feedback {
        background-color: #ffffff;
        color: #333;
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        border: 1px solid #ddd;
    }
    .btn-submit {
        background-color: #4B0082;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    .btn-submit:hover {
        background-color: #360061;
    }
    </style>
    """, unsafe_allow_html=True)

# User input for the question
question = st.text_input("Ask a question about your execution summary:", value="", key="question_input", placeholder="Type your question here...")

# Handle user input and get response from the chatbot
if st.button("Submit", key="submit_button"):
    if question:
        with st.spinner('Fetching results from the database...'):
            chain = get_few_shot_db_chain()
            response = chain.run(question)

            # Update conversation history
            st.session_state.conversation_history.append((question, response))

            # Keep only the last 5 conversations
            if len(st.session_state.conversation_history) > 5:
                st.session_state.conversation_history = st.session_state.conversation_history[-5:]

            # Display conversation history
            st.header("🗂️ Conversation History")
            for idx, (q, r) in enumerate(st.session_state.conversation_history[::-1]):
                st.markdown(f"<div class='chat-container'><div class='user-message'><strong>User:</strong> {q}</div><div class='bot-message'><strong>Bot:</strong> {r}</div></div>", unsafe_allow_html=True)

            # Display the response to the current question
            st.header("💡 Answer")
            st.write(response)

            # Clear the input field for new query
            question = ""

# Feedback section
st.header("📝 Feedback")
feedback = st.text_area("We value your feedback. Please provide your comments below:", value="", placeholder="Type your feedback here...")
if st.button("Submit Feedback", key="feedback_button"):
    if feedback.strip():
        st.session_state.feedback.append(feedback)
        st.success("Thank you for your feedback!")
    else:
        st.error("Feedback cannot be empty.")

# Footer
st.markdown("<footer><p style='text-align: center; color: #aaa;'>© 2024 Execution Summary Chatbot. All rights reserved.</p></footer>", unsafe_allow_html=True)










