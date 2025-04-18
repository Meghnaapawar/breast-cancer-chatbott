function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    const language = document.getElementById('language').value;
    const chatBox = document.getElementById('chat-box');
  
    chatBox.innerHTML += `<div><strong>You:</strong> ${userInput}</div>`;
  
    fetch('http://127.0.0.1:5000/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: userInput, language: language })
    })
    .then(res => res.json())
    .then(data => {
      chatBox.innerHTML += `<div><strong>Bot:</strong> ${data.reply}</div>`;
      chatBox.scrollTop = chatBox.scrollHeight;
    });
  
    document.getElementById('user-input').value = '';
  }
  
  function loadHospitals() {
    fetch('http://127.0.0.1:5000/hospitals')
      .then(res => res.json())
      .then(data => {
        const list = document.getElementById('hospital-list');
        list.innerHTML = '';
        data.forEach(hospital => {
          const item = document.createElement('li');
          item.textContent = `${hospital['Hospital Name']} (${hospital.City}, ${hospital.State}) - ${hospital.Type}`;
          list.appendChild(item);
        });
      });
  }
  