document.getElementById('query-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    var questionInput = document.getElementById('question-input');
    var spinner = document.getElementById('spinner');
    
    if (questionInput.value.trim() === "") {
        alert("Please enter a question.");
        return;
    }
    
    spinner.style.display = 'block';
    
    fetch('/submit_query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question: questionInput.value })
    })
    .then(response => response.json())
    .then(data => {
        spinner.style.display = 'none';
        
        var conversationHistory = document.getElementById('conversation-history');
        var currentAnswer = document.getElementById('current-answer');
        
        // Append to conversation history
        var userMessage = document.createElement('div');
        userMessage.className = 'user-message';
        userMessage.innerHTML = `<strong>User:</strong> ${questionInput.value}`;
        
        var botMessage = document.createElement('div');
        botMessage.className = 'bot-message';
        botMessage.innerHTML = `<strong>Bot:</strong> ${data.response}`;
        
        conversationHistory.appendChild(userMessage);
        conversationHistory.appendChild(botMessage);
        
        // Update current answer
        currentAnswer.innerHTML = `<h2>💡 Answer</h2><div>${data.response}</div>`;
        
        // Clear the input
        questionInput.value = '';
    })
    .catch(error => {
        spinner.style.display = 'none';
        console.error('Error:', error);
    });
});

document.getElementById('feedback-submit').addEventListener('click', function() {
    var feedbackInput = document.getElementById('feedback-input');
    
    if (feedbackInput.value.trim() === "") {
        alert("Feedback cannot be empty.");
        return;
    }
    
    fetch('/submit_feedback', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ feedback: feedbackInput.value })
    })
    .then(response => response.json())
    .then(data => {
        alert("Thank you for your feedback!");
        feedbackInput.value = '';
    })
    .catch(error => {
        console.error('Error:', error);
    });
});




