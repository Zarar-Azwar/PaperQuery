// static/script.js
document.addEventListener('DOMContentLoaded', () => {
    let messages = [];

    async function sendMessage() {
        const input = document.getElementById('userInput');
        const message = input.value.trim();
        
        if (!message) return;
        
        // Add user message
        addMessage('user', message);
        input.value = '';

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message }),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            
            // Format the assistant's response
            const formattedResponse = `# **Context**: \n${data.context}\n\n\n\n# **Answer**: \n${data.answer}`;
            
            // Add assistant message
            addMessage('assistant', formattedResponse);
        } catch (error) {
            console.error('Error:', error);
            addMessage('assistant', 'Sorry, there was an error processing your request.');
        }
    }

    function addMessage(role, content) {
        const chatContainer = document.getElementById('chatContainer');
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${role}-message`;
        
        // Convert markdown to HTML using marked library
        messageDiv.innerHTML = marked.parse(content);
        
        chatContainer.appendChild(messageDiv);
        chatContainer.scrollTop = chatContainer.scrollHeight;
        
        // Store message in history
        messages.push({ role, content });
    }

    // Handle Enter key in input
    document.getElementById('userInput').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    // Add click handler for send button
    document.getElementById('sendButton').addEventListener('click', sendMessage);

    // Make sendMessage available globally
    window.sendMessage = sendMessage;
});