from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)

# Enable CORS for all routes
CORS(app, origins=["http://localhost:5173"])

RASA_SERVER_URL = "http://localhost:5005/webhooks/rest/webhook"

@app.route('/test', methods=['POST'])
def handle_data():
    request_data = request.get_json().get("text")
    if not request_data:
        return jsonify({"Error:": "No message provided"}), 400

    rasa_response = requests.post(
        RASA_SERVER_URL,
        json={"sender": "test", "message": request_data}
    )

    if rasa_response.status_code == 200:
        rasa_data = rasa_response.json()

        # Extracting intent is easily possible using two calls to rasa
        # One to webhooks/rest/webhook, one to model/parse
        # intent = rasa_response.json().get("intent", {})
        # confidence_score = intent.get("confidence", None) 
        # print(confidence_score)

        print(rasa_data)
        response = {"content": rasa_data}

        return jsonify(response)
    else:
        return jsonify({"Error": "Failed to connect to Rasa"}), 400

if __name__ == '__main__':
    app.run(port=5001, debug=True)
