import React, { useEffect, useRef } from 'react';
import ReactMarkdown from 'react-markdown';


function ChatMessages ({messages}) {

    const chatContainerRef = useRef(null);

    // Auto-scroll to the bottom when messages change
    useEffect(() => {
        if (chatContainerRef.current) {
            chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
        }
    }, [messages]);

    return (
        <>
        
        <div className="chat-container" ref={chatContainerRef}>
            <div className="messages">

                <div className="chat-bubble ai-bubble">
                    <ReactMarkdown>Hi, I am your Calendar Assistant. How can I help you?</ReactMarkdown>
                    </div>

                {messages.map((msg, index) => (
                    <div
                        key={index}
                        className={`chat-bubble ${msg.sender === 'user' ? 'user-bubble' : 'ai-bubble'}`}
                    > 
                    <ReactMarkdown>{msg.text}</ReactMarkdown>
                
                </div>
            ))}

            </div>
        </div>
        
        </>
    )

}

export default ChatMessages