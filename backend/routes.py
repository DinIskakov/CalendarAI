from flask import Flask, jsonify, request
from flask_cors import CORS
from main import execute, authenticate


app = Flask(__name__)
cors = CORS(app, allow_origins="*")


@app.route("/process", methods=["POST"])
def process_input():
    data = request.json
    user_input = data.get("text", "")
    response = execute(user_input).get("output")
    
    return response




@app.route("/chat", methods=["POST"])
def ask_question():
    #Send the message to the AI Agent
    
    user_question = request.form.get("question", "")
    response = execute(user_question).get("output")

    return f"""
        <html>
            <body>
                <p>You asked: {user_question}</p>
                <p>Answer: {response}</p>
                <a href="/chat">Ask another</a>
            </body>
        </html>
    """

@app.route("/chat", methods=["GET"])
def answer():
    # Return the answer
    return """
        <html>
            <body>
                <h2>Ask a question</h2>
                <form method="POST">
                    <input type="text" name="question" placeholder="Enter your question" />
                    <input type="submit" value="Submit" />
                </form>
            </body>
        </html>
    """


if __name__ == '__main__':
    authenticate()
    app.run(debug=True)