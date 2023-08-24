const chatContainer = document.getElementById("chatContainer");
const contextContainer = document.getElementById("contextContainer")
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
      const sources = data.source_documents;  // Collect source documents
      console.log(sources);


      appendMessage("assistant", assistantResponse);  // Simulate assistant response

      for (const document of sources) {  // Access source documents
        appendSource(document);}

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

function appendSource(sourceDocument) {
  const docDiv = document.createElement("div");
  docDiv.classList.add("message", `context-message`);

    // Create content element
  const contentElement = document.createElement("div");
  contentElement.classList.add("content-line");
  contentElement.textContent = sourceDocument.page_content;
  docDiv.appendChild(contentElement);

  // Create source element
  const sourceElement = document.createElement("div");
  sourceElement.classList.add("source-line");
  sourceElement.textContent = "Source: " + sourceDocument.metadata.source; // Assuming metadata has a source property
  docDiv.appendChild(sourceElement);

  /*docDiv.textContent = sourceDocument.page_content;*/
  contextContainer.appendChild(docDiv);
  contextContainer.scrollTop = contextContainer.scrollHeight;
}
