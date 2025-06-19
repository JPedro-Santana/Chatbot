const input = document.getElementById("input");
const chat = document.getElementById("chat");
const sendBtn = document.getElementById("sendBtn");
const chatBox = document.getElementById("chatBox");

function toggleChat() {
  chatBox.style.display = chatBox.style.display === "flex" ? "none" : "flex";
}

function addMessage(text, sender = "bot") {
  const msg = document.createElement("div");
  msg.className = `message ${sender}`;
  msg.innerText = text;
  chat.appendChild(msg);
  chat.scrollTop = chat.scrollHeight;
}

sendBtn.onclick = async () => {
  const pergunta = input.value.trim();
  if (!pergunta) return;

  addMessage(pergunta, "user");
  input.value = "";

  try {
    const res = await fetch("http://localhost:5000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ mensagem: pergunta })
    });
    const data = await res.json();
    addMessage(data.resposta);
  } catch (err) {
    addMessage("Desculpe, não consegui ligar-me ao meu cérebro. Verifique se o backend está a correr.");
  }
};