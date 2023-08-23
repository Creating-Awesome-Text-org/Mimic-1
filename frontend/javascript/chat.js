const chatContainer = document.getElementById("chatContainer");
const userInput = document.getElementById("userInput");
const sendMessageBtn = document.getElementById("sendMessageBtn");

sendMessageBtn.addEventListener("click", sendMessage);

function sendMessage() {
  const userMessage = userInput.value;
  if (userMessage.trim() !== "") {
    appendMessage("user", userMessage);
    userInput.value = "";
    // Simulate assistant response after a short delay
    setTimeout(() => {
      appendMessage("assistant", "Hi there! I'm here to assist.");
    }, 500);
  }
}

function appendMessage(sender, message) {
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("message", `${sender}-message`);
  messageDiv.textContent = message;
  chatContainer.appendChild(messageDiv);
  chatContainer.scrollTop = chatContainer.scrollHeight; // Scroll to bottom
}
