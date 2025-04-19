import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the QA data from the JSON file
with open('qa_data.json', 'r') as f:
    qa_data = json.load(f)

# Route for the chatbot interaction
@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question')
    
    # Simple matching for answers (you can expand this logic)
    answer = qa_data.get(question.lower(), "Sorry, I don't have an answer for that.")
    
    return jsonify({"answer": answer})

# If running locally, listen on the correct port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
