from flask import Flask, render_template, request, redirect, url_for
from langchain_helper import get_few_shot_db_chain
import os

app = Flask(__name__)

# Initialize session state for storing conversation history and feedback
conversation_history = []
feedback_list = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form.get('question')
        if question:
            chain = get_few_shot_db_chain()
            response = chain.run(question)
            conversation_history.append((question, response))
            if len(conversation_history) > 5:
                conversation_history.pop(0)
        return render_template('index.html', conversation_history=conversation_history, response=response)
    return render_template('index.html', conversation_history=conversation_history)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        feedback = request.form.get('feedback')
        if feedback.strip():
            feedback_list.append(feedback)
            return redirect(url_for('feedback'))
    return render_template('feedback.html', feedback_list=feedback_list)

if __name__ == '__main__':
    app.run(debug=True)











