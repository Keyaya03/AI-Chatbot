import { useState } from "react";
import ChatInput from "./ChatInput"

function ChatWindow() {
const [messages, setMessages] = useState([]);

const handleSend = async (question) => {
const userMessage = { sender: "user", text: question };
setMessages((prev) => [...prev, userMessage]);

const response = await fetch("http://127.0.0.1:8000/chat", {
method: "POST",
headers: { "Content-Type": "application/json" },
body: JSON.stringify({ question: question }),
});

const data = await response.json();
const botMessage = { sender: "bot", text: data.answer };
setMessages((prev) => [...prev, botMessage]);
};

return (
  <div>
    <h5>Chat Bot</h5>
    {messages.map((msg, index) => (
      <p key={index}>
        <strong>{msg.sender}:</strong> {msg.text}
      </p>
    ))}
    <ChatInput onSend={handleSend} />
  </div>
);
}

export default ChatWindow;