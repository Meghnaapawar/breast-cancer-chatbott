import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load your Q&A data from the JSON file
with open('qa_data.json', 'r') as f:
    qa_data = json.load(f)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    language = request.json.get('language')

    # Match the user input to an answer
    for qa in qa_data['qna']:
        if user_message.lower() in qa['question'].lower():
            response = qa['answer']
            break
    else:
        response = "Sorry, I don't understand the question."

    return jsonify({'reply': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
