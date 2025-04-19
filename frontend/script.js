document.addEventListener("DOMContentLoaded", function () {
  const chatbox = document.getElementById("chatbox");
  const userInput = document.getElementById("user-input");
  const sendButton = document.getElementById("send-button");

  async function fetchChatResponse(userText) {
    try {
      const response = await fetch('/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question: userText })
      });

      const data = await response.json();
      appendMessage(`Bot: ${data.answer}`);
    } catch (err) {
      console.error("Error:", err);
      appendMessage("Bot: Sorry, something went wrong.");
    }
  }

  function appendMessage(text) {
    const msg = document.createElement("div");
    msg.textContent = text;
    chatbox.appendChild(msg);
  }

  sendButton.addEventListener("click", () => {
    const userText = userInput.value.trim();
    if (userText === "") return;
    appendMessage(`You: ${userText}`);
    fetchChatResponse(userText);
    userInput.value = "";
  });

  async function loadHospitals() {
    try {
      const response = await fetch('/hospitals');
      const data = await response.json();
      const hospitalDiv = document.getElementById("hospitals");
      hospitalDiv.innerHTML = data.hospitals.map(h => `<li>${h.name}</li>`).join('');
    } catch (err) {
      console.error("Error loading hospitals:", err);
    }
  }

  loadHospitals();
});
