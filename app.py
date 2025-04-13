from flask import Flask, request, jsonify
from chatbot.chatbot import ai_chatbot
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

@app.route("/")
def home():
    return "AI Chatbot is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    response = ai_chatbot(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
