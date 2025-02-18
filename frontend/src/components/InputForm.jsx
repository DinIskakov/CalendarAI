import { useState, useEffect } from 'react'
import axios from 'axios'

function InputForm() {
    const [input, setInput] = useState("")
    const [response, setResponse] = useState(""); // State to store the backend response
    

    const sendInputToBackend = async (e) => {
        e.preventDefault(); // Prevent form submission
        if (input.trim() === "") return; // Don't send empty input

        try {
            // Send a POST request to the Flask backend
            const result = await axios.post("http://127.0.0.1:5000/process", { text: input,});
            

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
    
        <form className="input-form" onSubmit={sendInputToBackend}>
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type your question..."
          />
          <button>
            ➤
          </button>
        </form>

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
    
        </>
      )

}

export default InputForm;