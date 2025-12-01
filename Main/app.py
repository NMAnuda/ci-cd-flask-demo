from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/predict")
def predict():
    value = request.args.get("value", type=float)
    if value is None:
        return jsonify({"error": "Missing value parameter"}), 400

    prediction = value * 2
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
