from flask import Flask, request, jsonify, render_template, send_from_directory
import json
import os

app = Flask(__name__, static_folder='frontend', template_folder='frontend')

# Load QnA data
with open('qa_data.json', 'r', encoding='utf-8') as f:
    qna_data = json.load(f)

# Load hospital data
with open('hospitals.json', 'r', encoding='utf-8') as f:
    hospital_data = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data.get('question', '').lower()
    for item in qna_data:
        if question in item['question'].lower():
            return jsonify({'answer': item['answer']})
    return jsonify({'answer': 'Sorry, I do not understand your question.'})

@app.route('/hospitals', methods=['GET'])
def get_hospitals():
    return jsonify({'hospitals': hospital_data})

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('frontend', path)

if __name__ == '__main__':
    app.run(debug=True)
