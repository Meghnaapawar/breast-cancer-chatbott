import json
from flask import Flask, request, jsonify
import difflib

app = Flask(__name__)

# Function to load the questions and answers from JSON file
def get_answer_from_json(question):
    try:
        with open("qa_data.json", "r") as file:
            data = json.load(file)

        question_lower = question.strip().lower()
        for item in data:
            if item["question"].strip().lower() == question_lower:
                return item["answer"]
        return "🤖 I'm sorry, I don't have an answer for that yet."
    except FileNotFoundError:
        return "Error: qa_data.json not found."
    except json.JSONDecodeError:
        return "Error: Invalid JSON format."

# Route to handle chat requests
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message")
    
    if not user_input:
        return jsonify({"response": "⚠️ Please provide a message."})

    # Get the response based on the user's question
    response = get_answer_from_json(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
