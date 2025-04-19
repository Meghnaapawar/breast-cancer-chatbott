document.getElementById('send-btn').addEventListener('click', async () => {
  const inputField = document.getElementById('user-input');
  const userText = inputField.value.trim();

  if (!userText) return;

  appendMessage(`You: ${userText}`);

  const response = await fetch('/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question: userText })
  });

  const data = await response.json();
  appendMessage(`Bot: ${data.answer}`);

  inputField.value = '';
});

document.getElementById('show-hospitals').addEventListener('click', async () => {
  const response = await fetch('/hospitals');
  const data = await response.json();
  const hospitals = data.hospitals;

  if (hospitals && hospitals.length > 0) {
    let hospitalList = 'Hospitals:\n';
    hospitals.forEach((h, i) => {
      hospitalList += `${i + 1}. ${h.name} - ${h.city}\n`;
    });
    appendMessage(hospitalList);
  } else {
    appendMessage('No hospitals found.');
  }
});

function appendMessage(message) {
  const chatBox = document.getElementById('chat-box');
  const msgElement = document.createElement('div');
  msgElement.textContent = message;
  chatBox.appendChild(msgElement);
}
