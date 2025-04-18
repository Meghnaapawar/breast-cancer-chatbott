from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import json

app = Flask(__name__)
CORS(app)

# Load Q&A data
with open('qa_data.json', 'r', encoding='utf-8') as f:
    qa_pairs = json.load(f)

# Load hospital data
hospitals = pd.read_csv('Breast_Cancer_Hospitals_India.csv')

def search_answer(user_input):
    for pair in qa_pairs:
        if pair['question'].lower() in user_input.lower():
            return pair['answer']
    return "Sorry, I couldn’t find an answer. Please consult a doctor."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message", "")
    language = data.get("language", "English")

    # Basic response
    answer = search_answer(user_input)

    # Language support (fake for now, real translation coming next)
    if language == "Hindi":
        answer = "यह उत्तर हिंदी में है: " + answer
    elif language == "Marathi":
        answer = "हा उत्तर मराठीत आहे: " + answer

    return jsonify({"reply": answer})

@app.route('/hospitals', methods=['GET'])
def get_hospitals():
    return hospitals.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)
