from flask import Flask, request
from main import execute, authenticate

app = Flask(__name__)

'''@app.route("/")
def assistant():
    #response = execute("Hello how are you")
    #print(response.get("output"))
    ans = execute("Hello how are you")
    return ans'''

@app.route("/", methods=["GET", "POST"])
def assistant():
    if request.method == "POST":
        # Get the user’s input from the form
        user_question = request.form.get("question", "")
        # Call your model here (e.g., "execute(user_question)")
        response = execute(user_question).get("output")
        # Return some page displaying the answer
        return f"""
            <html>
                <body>
                    <p>You asked: {user_question}</p>
                    <p>Answer: {response}</p>
                    <a href="/">Ask another</a>
                </body>
            </html>
        """

    # If GET request, show the form
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
    app.run()