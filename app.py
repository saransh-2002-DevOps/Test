# app.py

from flask import Flask, jsonify
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
# Enable CORS for the entire application to allow requests from the frontend
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    """
    API endpoint to return sample data.
    The data is a simple dictionary which will be converted to JSON.
    """
    data = {
        "message": "Hello from the Python backend!",
        "version": "1.0",
        "timestamp": "2025-08-24T08:00:00Z"
    }
    # Return the data as a JSON response
    return jsonify(data)

if __name__ == '__main__':
    # Run the application on a specific host and port.
    # debug=True allows for automatic reloading on code changes.
    app.run(host='0.0.0.0', port=5000, debug=True)
