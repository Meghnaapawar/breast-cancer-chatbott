from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Load qa_data.json file
with open('qa_data.json', 'r') as file:
    qa_data = json.load(file)

# Dummy function to handle user input and provide response from qa_data.json
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')  # Get the user input from frontend
    language = request.json.get('language')  # Get the selected language (if needed)

    # Loop through qa_data to find a matching question
    for entry in qa_data['qa']:
        if entry['question'].lower() in user_input.lower():
            response = entry['answer']
            break
    else:
        response = "Sorry, I don't understand that question."

    # Return the response to the frontend
    return jsonify({'reply': response})

# Hospital data endpoint (you can modify as per your hospitals.json structure)
@app.route('/hospitals', methods=['GET'])
def hospitals():
    hospitals = [
        "Tata Memorial Hospital, Mumbai",
        "AIIMS, Delhi",
        "Apollo Hospitals",
        "Fortis Healthcare",
        "Max Healthcare"
    ]
    return jsonify(hospitals)

if __name__ == '__main__':
    app.run(debug=True)
