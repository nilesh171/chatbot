from flask import Flask, render_template, request, jsonify
from model import generate_response

app = Flask(__name__)

# Route to serve the main chatbot interface
@app.route('/')
def index():
    return render_template('chatbot.html')

# API endpoint to handle chatbot responses
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    bot_response = generate_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
