

import os
from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": "Learn Git",
        "status": "completed"
    },
    {
        "id": 2,
        "title": "Create Dockerfile",
        "status": "in progress"
    },
    {
        "id": 3,
        "title": "Deploy application",
        "status": "pending"
    }
]


@app.route("/")
def home():
    return jsonify({
        "application": "BuildLabs DevOps Task Manager",
        "message": "Application is running successfully",
        "version": "1.0.0"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/tasks")
def get_tasks():
    return jsonify(tasks)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)