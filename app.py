from flask import Flask, render_template, request, jsonify
from datetime import datetime
import random

# Flask app must be defined FIRST
app = Flask(__name__)

# ---------------- CHATBOT LOGIC ----------------
def chatbot_response(user):
    user = user.lower()

    if user in ["hi", "hello", "hey"]:
        return "Hello! 👋 How can I help you?"

    elif "how are you" in user:
        return "I'm doing great! 😎 Thanks for asking."

    elif "your name" in user:
        return "My name is SmartBot 🤖"

    elif "creator" in user:
        return "I was created by Hashim using Python and Flask 🚀"

    elif "python" in user:
        return "Python is a powerful programming language used in AI, Web Development and Data Science."

    elif "flask" in user:
        return "Flask is a lightweight Python web framework."

    elif "time" in user:
        return f"Current time is {datetime.now().strftime('%H:%M:%S')}"

    elif "date" in user:
        return f"Today's date is {datetime.now().strftime('%d-%m-%Y')}"

    elif "joke" in user:
        return "Why do programmers love dark mode? Because light attracts bugs! 😂"

    elif "motivate" in user:
        return "Success is the sum of small efforts repeated every day. 🚀"

    elif "fact" in user:
        return "Did you know? Python was named after Monty Python, not the snake!"

    elif "help" in user:
        return """
Available Commands:
- hi / hello
- how are you
- time
- date
- joke
- python
- flask
- creator
- motivate
- fact
- help
"""

    elif user == "exit":
        return "Goodbye! 👋 Have a great day."

    else:
        return random.choice([
            "🤔 Interesting! Tell me more.",
            "😅 I don't understand that yet.",
            "💡 Try typing 'help'.",
            "🚀 I'm still learning new things."
        ])

# ---------------- ROUTES ----------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_message = request.form["message"]
    return jsonify({"response": chatbot_response(user_message)})

# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    print("App started 🚀")
    app.run(debug=True)