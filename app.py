from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def get_home():
    return jsonify({"message": "Api no ar!"})