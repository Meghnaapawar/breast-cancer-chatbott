from flask import Flask, request, jsonify, send_from_directory
import json
import os
import difflib

app = Flask(__name__)

# Load QnA and hospitals data
with open('qa_data.json', 'r', encoding='utf-8') as f:
    qna_data = json.load(f)

with open('hospitals.json', 'r', encoding='utf-8') as f:
    hospital_data = json.load(f)

# Serve frontend
@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('frontend', filename)

# Chatbot route
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('question', '').strip().lower()
    for pair in qna_data:
        if user_input == pair['question'].lower():
            return jsonify({'answer': pair['answer']})
    return jsonify({'answer': "I'm sorry, I don't have an answer for that. Please consult a doctor."})

# Hospitals route
@app.route('/hospitals', methods=['GET'])
def get_hospitals():
    return jsonify({'hospitals': hospital_data})

if __name__ == '__main__':
    app.run(debug=True)
