from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! This is your free server on Render!"

@app.route('/api', methods=['POST'])
def api():
    data = request.json
    return jsonify({"received": data, "status": "success"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
