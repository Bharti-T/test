from flask import Flask, jsonify
from printing import get_greeting

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "success",
        "message": get_greeting()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)