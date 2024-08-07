#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views  # Ensure this path matches your directory structure
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Register the blueprint with the URL prefix
app.register_blueprint(app_views, url_prefix='/api/v1')

# Enable CORS for all routes under /api/v1/*
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    # Get host and port from environment variables or use defaults
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)  # Enable debug mode
