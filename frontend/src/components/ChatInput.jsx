import { useState } from "react";

function ChatInput({ onSend }) {
  const [text, setText] = useState("");

  const handleSend = () => {
    if (text.trim() === "") return;
    onSend(text);
    setText("");
  };

  return (
    <div>
        <input type="text" value={text} onChange={(e) => setText(e.target.value)}/>
        <button onClick={handleSend}>Send</button>
    </div>
  );
}

export default ChatInput;