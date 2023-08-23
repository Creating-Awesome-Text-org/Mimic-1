const chatContainer = document.getElementById("chatContainer");
const userInput = document.getElementById("userInput");
const sendMessageBtn = document.getElementById("sendMessageBtn");
const endpoint_root = "http://127.0.0.1:8000";

sendMessageBtn.addEventListener("click", sendMessage);

function sendMessage() {
  const userMessage = userInput.value;
  if (userMessage.trim() !== "") {
    appendMessage("user", userMessage);
    userInput.value = "";

    const requestData = {
      question: userMessage
    }; //Create the expected JSON object

    fetch(endpoint_root + '/qa_question', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(requestData)
    })
    .then(response => response.json())
    .then(data => {
      const assistantResponse = data.result; // Adjust based on the actual response structure
      appendMessage("assistant", assistantResponse);  // Simulate assistant response
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }
}

function appendMessage(sender, message) {
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("message", `${sender}-message`);
  messageDiv.textContent = message;
  chatContainer.appendChild(messageDiv);
  chatContainer.scrollTop = chatContainer.scrollHeight; // Scroll to bottom
}
