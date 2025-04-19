from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ✅ Serve the chatbot page
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# 🧠 Chat endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message")

    if not user_input:
        return jsonify({"response": "⚠️ Please provide a message."})

    # Placeholder chatbot logic
    response = f"You said: {user_input} — this is a placeholder response."

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
