from flask import Flask, request, jsonify
from model import predict

app = Flask(__name__)

@app.route("/")
def home():
    return "ML model is up and running!"

@app.route("/predict", methods=["POST"])
def predict_route():
    data = request.json
    features = data.get("features")
    pred = predict(features)
    return jsonify({"prediction": pred})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
