import json
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

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

@app.route("/api/contact", methods=["POST"])
def handle_contact():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not name or not email or not message:
        return jsonify({"error": "All fields must be filled out"}), 400
    
    EMAIL_USER = os.getenv('EMAIL_USER')
    EMAIL_PASS = os.getenv('EMAIL_PASS')

    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_USER
    msg['Subject'] = f"New portfolio message from: {name}" 

    body = f"Name: {name}\nE-MAIL: {email}\n\nMessage:\n{message}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        text = msg.as_string()
        server.sendmail(EMAIL_USER, EMAIL_USER, text)
        server.quit()
        return jsonify({"message": "Message successfuly sent"}), 200
    except Exception as e:
        print(e)
        return jsonify({"erro": "An error ocurred when sending the message"}), 500

if __name__ == "__main__":
    app.run(debug=True)