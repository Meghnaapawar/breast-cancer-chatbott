from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ✅ Home route to confirm the app is live
@app.route("/")
def home():
    return "✅ Breast Cancer Chatbot is live and ready to help!"

# 🧠 Chatbot route
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message")

    if not user_input:
        return jsonify({"response": "⚠️ Please provide a message."})

    # Replace this logic with your chatbot's actual response mechanism
    # For now, it's just a placeholder
    response = f"You said: {user_input} — this is a placeholder response."

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
