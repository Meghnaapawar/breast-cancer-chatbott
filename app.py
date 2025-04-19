from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import difflib

app = Flask(__name__)
CORS(app)

# Load the QnA data
with open("qa_data.json", "r") as file:
    qa_data = json.load(file)

def get_answer_from_json(question):
    questions = [item["question"] for item in qa_data]
    closest_match = difflib.get_close_matches(question.lower(), [q.lower() for q in questions], n=1, cutoff=0.4)

    if closest_match:
        for item in qa_data:
            if item["question"].lower() == closest_match[0]:
                return item["answer"]
    return "🤔 Sorry, I couldn't find an answer for that. Try rephrasing your question."

@app.route("/")
def home():
    return "✅ Breast Cancer Chatbot is live and ready to help!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message")

    if not user_input:
        return jsonify({"response": "⚠️ Please provide a message."})

    try:
        response = get_answer_from_json(user_input)
    except Exception as e:
        response = f"❌ Error: {str(e)}"

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=False, port=10000)
