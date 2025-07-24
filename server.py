# server.py
# This is a simple web server using the Flask framework.
# It listens for POST requests on the /api/device endpoint.

from flask import Flask, request, jsonify
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("device_api")

# Initialize the Flask application
app = Flask(__name__)

@app.route('/api/device', methods=['POST'])
def receive_device_info():
    """
    This function handles incoming POST requests to /api/device.
    It expects a JSON payload with device information.
    """
    # Check if the incoming request contains JSON data
    if not request.is_json:
        logger.warning("Non-JSON request")
        # Return an error response
        return jsonify({"status": "error", "message": "Request must be JSON"}), 400

    data = request.get_json(silent=True)  # avoid exceptions
    if data is None:
        logger.warning("Malformed JSON")
        return jsonify({"status": "error", "message": "Malformed JSON"}), 400

    logger.info("Device payload: %s", data)

    # Extract the information from the JSON data
    # It's good practice to use .get() to avoid errors if a key is missing
    device_name = data.get('deviceName')
    model = data.get('model')
    manufacturer = data.get('manufacturer')
    ip_address = data.get('ipAddress')

    # --- Your Logic Here ---
    # For now, we'll just print the received information to the console.
    # In a real application, you might save this to a database,
    # write it to a file, or perform other actions.
    print("---------------------------------")
    print(f"Received Device Info:")
    print(f"  Device Name: {device_name}")
    print(f"  Model: {model}")
    print(f"  Manufacturer: {manufacturer}")
    print(f"  IP Address: {ip_address}")
    print("---------------------------------")
    
    # Send a success response back to the Android app
    response_data = {
        "status": "success",
        "message": "Device information received successfully."
    }
    return jsonify(response_data), 200

if __name__ == '__main__':
    # Run the app.
    # host='0.0.0.0' makes the server accessible from any device on the network.
    # port=5000 is the port number we'll listen on.
    # debug=True provides helpful error messages during development.
    app.run(host='0.0.0.0', port=5000, debug=True)
