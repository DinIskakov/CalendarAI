import { useState, useEffect } from 'react'
import './App.css'
import InputForm from './components/InputForm'
import ChatMessages from './components/ChatMessages'
import axios from 'axios'


function App() {

  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("")

  /*useEffect(() => {
    console.log('Messages updated:', messages);
  }, [messages]);*/
    
  const sendInputToBackend = async (e) => {
    e.preventDefault(); // Prevent form submission
    if (input.trim() === "") return; // Don't send empty input

    const userMessage = { sender: 'user', text: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");

    console.log(userMessage)

    try {
        // Send a POST request to the Flask backend
        const result = await axios.post("http://127.0.0.1:5000/process", { text: input });
        

        const aiMessage = { sender: 'ai', text: result['data'] };
        
        setMessages((prev) => [...prev, aiMessage]);

        
        console.log(result['data'])
        
    } catch (error) {
        console.error("Error sending input to backend:", error);
    }

    // Clear the input field
  };  
  

  return (
    <>
    <div className="chat-app">
      <ChatMessages messages={messages}/>
      <InputForm
        inputValue={input}
        onChange={(e) => setInput(e.target.value)}
        onSubmit={sendInputToBackend}
      />
    </div>
    </>
  )
}

export default App
