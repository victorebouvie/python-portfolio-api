# Portfolio API (Python/Flask)

![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python)
![Framework](https://img.shields.io/badge/Framework-Flask-black?style=for-the-badge&logo=flask)
![Type](https://img.shields.io/badge/Type-REST_API-green?style=for-the-badge&logo=json)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

A lightweight RESTful API built with Flask to serve portfolio project data from a JSON file and handle contact form submissions via email.

---

## 📋 Table of Contents

*   [About The Project](#-about-the-project)
*   [Key Features](#-key-features)
*   [Architecture (How It Works)](#️-architecture-how-it-works)
*   [Getting Started](#-getting-started)
    *   [Prerequisites](#prerequisites)
    *   [Installation](#installation)
*   [API Endpoints](#%EF%B8%8F-api-endpoints)
    *   [Get Projects](#get-apiprojects)
    *   [Submit Contact Form](#post-apicontact)
*   [Project Structure](#-project-structure)

---

## 📖 About The Project

This API serves as the backend for a dynamic portfolio website. Instead of hardcoding project details into the frontend, this service provides the data through a simple REST endpoint. This decouples the data from the presentation layer, making the portfolio much easier to manage and update.

Additionally, it includes a contact form endpoint that processes user messages and forwards them to a designated email address using SMTP, eliminating the need for a third-party email service for a simple portfolio site. The entire application is self-contained and designed to be lightweight and easily deployable.

---

## ✨ Key Features

*   ✅ **Dynamic Project Data**: Serves portfolio projects from a simple `projects.json` file, making it easy to add, remove, or edit projects without touching the application code.
*   ✅ **Contact Form Backend**: Provides a `POST` endpoint to handle contact form submissions, sending the details directly to your email.
*   ✅ **Secure Credential Handling**: Uses a `.env` file to securely store email credentials, keeping them out of the source code.
*   ✅ **CORS Enabled**: Configured with `Flask-CORS` to allow cross-origin requests, making it compatible with any frontend framework hosted on a different domain.
*   ✅ **Minimal Dependencies**: Built with a minimal set of libraries (Flask, Flask-CORS, python-dotenv) for a lightweight footprint.
*   ✅ **Stateless Design**: The API is stateless, making it robust and simple to scale or deploy in containerized environments.

---

## ⚙️ Architecture (How It Works)

The API operates on a simple request-response cycle managed by Flask.

1.  **Initialization**: When the application starts, it initializes Flask and sets up CORS policies. Environment variables from the `.env` file are loaded.
2.  **Request Handling**: The server listens for incoming HTTP requests and routes them based on the URL and method.
3.  **Route: `GET /api/projects`**:
    *   When a `GET` request is received at this endpoint, the application opens the `projects.json` file.
    *   It reads the contents of the file, which is an array of project objects.
    *   The data is then serialized into a JSON format and sent back to the client with a `200 OK` status.
4.  **Route: `POST /api/contact`**:
    *   When a `POST` request is received, the application parses the JSON payload from the request body.
    *   It validates that `name`, `email`, and `message` fields are present.
    *   It retrieves the `EMAIL_USER` and `EMAIL_PASS` from the environment variables.
    *   Using Python's `smtplib`, it connects to an SMTP server (e.g., Gmail), authenticates, and sends the formatted message to the configured `EMAIL_USER`.
    *   A success or error JSON response is sent back to the client.

The data flow is as follows:
**Client (Frontend)** → **Flask API Request** → **File I/O (`projects.json`) or SMTP Service** → **JSON Response** → **Client (Frontend)**

---

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

*   **Python 3.8+**
*   **Pip** package manager
*   A **Gmail Account** with an **App Password** enabled. Standard passwords will not work due to Google's security policies. You can follow [Google's guide](https://support.google.com/accounts/answer/185833) to create one.

### Installation

1.  Clone the repository:
    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    ```
2.  Navigate to the project directory:
    ```sh
    cd your-repo-name
    ```
3.  Create and activate a virtual environment:
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```
4.  Install the required packages. Create a `requirements.txt` file with the following content:
    ```txt
    Flask
    Flask-Cors
    python-dotenv
    ```
    Then run:
    ```sh
    pip install -r requirements.txt
    ```
5.  Create a `.env` file in the root directory and add your email credentials:
    ```env
    EMAIL_USER="your-email@gmail.com"
    EMAIL_PASS="your-16-character-app-password"
    ```
6.  Ensure the `projects.json` file exists in the root directory with the correct data structure.

7.  Run the application:
    ```sh
    python app.py
    ```
    The API will now be running at `http://127.0.0.1:5000`.

---

## 🛠️ API Endpoints

The API provides the following endpoints.

### `GET /api/projects`

Retrieves the list of all portfolio projects.

*   **Method**: `GET`
*   **Success Response (200 OK)**:
    ```json
    [
        {
            "id": 1,
            "name": "Roblox Survival Horror Framework (Lua)",
            "description": "A modular and lightweight first-person equipment system...",
            "technologies": ["Lua", "Roblox Studio", "OOP"],
            "github_url": "https://github.com/victorebouvie/survivalhorror-framework",
            "live_url": ""
        }
    ]
    ```

### `POST /api/contact`

Submits a message from the contact form. The message is sent to the email address specified in the `.env` file.

*   **Method**: `POST`
*   **Headers**: `Content-Type: application/json`
*   **Request Body**:
    ```json
    {
      "name": "Jane Doe",
      "email": "jane.doe@example.com",
      "message": "Hello, I would like to connect with you."
    }
    ```
*   **Success Response (200 OK)**:
    ```json
    {
      "message": "Message successfuly sent"
    }
    ```
*   **Error Response (400 Bad Request)**: Returned if any of the fields are missing.
    ```json
    {
      "error": "All fields must be filled out"
    }
    ```
*   **Error Response (500 Internal Server Error)**: Returned if the SMTP server fails to send the email.
    ```json
    {
      "erro": "An error ocurred when sending the message"
    }
    ```
