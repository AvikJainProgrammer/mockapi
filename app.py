from flask import Flask, request, jsonify
import json
import time

app = Flask(__name__)

# Load the predefined responses
with open('responses.json') as f:
    responses = json.load(f)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('input')

    # Simulate lag
    time.sleep(data.get('lag', 0))  # 'lag' is in seconds

    response = responses.get(user_input, "Sorry, I don't understand.")

    return jsonify({'response': response})

@app.route('/status', methods=['GET'])
def status():
    return "API is running."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
