from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app, origins=["http://localhost:5173"])


@app.route('/test', methods=['POST'])
def handle_data():
    data = request.get_json()
    print(data)

    response = {"text": data}
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
