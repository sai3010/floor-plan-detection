# floor-plan-detection
REST API’s for accessing the locations of BLE and WiFi devices using Opencv python.

# How to run
- Create a virtual environment
    - `python3 -m venv venv`
- Activate the environment
    - `source venv/bin/activate`
- Upgrade pip
    - `pip install --upgrade pip`
- Install dependencies
    - `pip install -r requirements.txt`
- Start the server
    -  `python3 server.py`

# List of supported apis
- `Get` -> /api/devices
    -  `curl --location --request GET 'http://localhost:8000/api/devices/'`
- `Get` -> /api/devices/ble
    - `curl --location --request GET 'http://localhost:8000/api/devices/ble'`
- `Get` -> /api/devices/wifi
    - `curl --location --request GET 'http://localhost:8000/api/devices/wifi'`
- `Get` -> /api/devices/wifi/dev_id
    - `curl --location --request GET 'http://localhost:8000/api/devices/wifi/1'`
- `Get` -> /api/devices/ble/dev_id
    - `curl --location --request GET 'http://localhost:8000/api/devices/ble/1'`