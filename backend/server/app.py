from db import insert_user_input
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)

# Enable CORS for all routes
CORS(app, origins=["http://localhost:5173"])

RASA_SERVER_URL = "http://localhost:5005/webhooks/rest/webhook"
RASA_MODEL_URL = "http://localhost:5005/model/parse"

@app.route('/test', methods=['POST'])
def handle_data():

    request_data = request.get_json().get("text")
    if not request_data:
        return jsonify({"Error:": "No message provided"}), 400

    # Add user input to database
    insert_user_input(request_data)

    parse_response = requests.post(
        RASA_MODEL_URL,
        json={"text": request_data}
    )

    confidence = None
    if parse_response.status_code == 200:
        parse_data = parse_response.json()
        confidence = parse_data.get("intent", {}).get("confidence")

    rasa_response = requests.post(
        RASA_SERVER_URL,
        json={"sender": "test", "message": request_data}
    )

    if rasa_response.status_code == 200:
        rasa_data = rasa_response.json()

        response = {"confidence": confidence, "content": rasa_data}
        print(response)

        return jsonify(response)
    else:
        return jsonify({"Error": "Failed to connect to Rasa"}), 400

if __name__ == '__main__':
    app.run(port=5001, debug=True)
