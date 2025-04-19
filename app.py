from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import difflib
import os

app = Flask(__name__)
CORS(app)

# Load Q&A Data
with open("qa_data.json", "r", encoding="utf-8") as f:
    qa_data = json.load(f)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()

    # Extract all questions from the dataset
    questions = [item["question"].lower() for item in qa_data]

    # Find closest match to user's input
    match = difflib.get_close_matches(user_input, questions, n=1, cutoff=0.5)

    if match:
        matched_question = match[0]
        for item in qa_data:
            if item["question"].lower() == matched_question:
                return jsonify({"reply": item["answer"]})

    return jsonify({"reply": "Sorry, I couldn't find an answer. Please consult a doctor."})

# Run the server on the correct port
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
