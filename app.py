import json
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
@app.route("/")
def get_home():
    return jsonify({"message": "Api no ar!"})

@app.route("/api/projects")
def get_projects():
    with open('projects.json', 'r', encoding='utf-8') as file:
        projects_data = json.load(file)
    return jsonify(projects_data)

if __name__ == "__main__":
    app.run(debug=True)