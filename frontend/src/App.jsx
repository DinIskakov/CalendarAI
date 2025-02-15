import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from 'axios'

function App() {
  const [count, setCount] = useState(0)
  const [array, setArray] = useState([])

  const fetchAPI = async () => {
    const response = await axios("http://127.0.0.1:5000/api/users")
    console.log(response.data.users)
    setArray(response.data.users)
  }

  useEffect(() => {
    fetchAPI()
  }, [])
  


  const [input, setInput] = useState("")
  const [response, setResponse] = useState(""); // State to store the backend response

  const sendInputToBackend = async () => {
    if (input.trim() === "") return; // Don't send empty input

    try {
      // Send a POST request to the Flask backend
      const result = await axios.post("http://127.0.0.1:5000/process", {
        text: input,
      });

      // Set the response from the backend
      setResponse(result.data.response);
    } catch (error) {
      console.error("Error sending input to backend:", error);
      setResponse("Failed to get a response from the backend.");
    }

    // Clear the input field
    setInput("");
  };

  return (
    <>

    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        gap: "10px",
        marginTop: "20px",
      }}
    >
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyPress={(e) => e.key === "Enter" && sendInputToBackend()}
        placeholder="Type your question..."
        style={{
          padding: "10px",
          width: "300px",
          borderRadius: "5px",
          border: "1px solid #ccc",
        }}
      />
      <button
        onClick={sendInputToBackend}
        style={{
          padding: "10px 20px",
          borderRadius: "5px",
          border: "none",
          backgroundColor: "#007bff",
          color: "#fff",
          cursor: "pointer",
        }}
      >
        Send
      </button>
      {response && (
        <div
          style={{
            marginTop: "20px",
            padding: "10px",
            backgroundColor: "#f0f0f0",
            borderRadius: "5px",
            width: "300px",
            textAlign: "center",
            color: "#333",
          }}
        >
          <strong>Backend Response:</strong> {response}
        </div>
      )}
      </div>


      
      {/*<h1>Vite + React</h1>
      <div className="card">

        <button onClick={() => setCount((lll) => lll + 1)}>
          count is {count}
        </button>

        {array.map((user, index) => (
          <div key={index}>
          <span>{user}</span> 
          <br></br>
          </div>
        ))}
        
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>*/}
    </>
  )
}

export default App
