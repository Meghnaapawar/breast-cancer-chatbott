import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to load the questions and answers from JSON file
def get_answer_from_json(question):
    try:
        # Ensure you're loading the correct file
        with open("qa_data.json", "r") as file:
            data = json.load(file)
            print("Loaded data:", data)  # Debug: print the loaded JSON

        # Clean and match the user question
        question_lower = question.strip().lower()
        print("User question (lowercase):", question_lower)  # Debug: print cleaned user input

        for item in data:
            item_question = item["question"].strip().lower()
            print("Item question:", item_question)  # Debug: print item question

            if item_question == question_lower:
                print("Answer found:", item["answer"])  # Debug: print the found answer
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
