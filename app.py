from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (you can replace this with your own data source)
drivers = [
    {"id": 1, "name": "Lewis Hamilton", "wins": 95, "poles": 98},
    {"id": 2, "name": "Sebastian Vettel", "wins": 53, "poles": 57},
    {"id": 3, "name": "Ayrton Senna", "wins": 41, "poles": 65}
]

@app.route('/api/drivers', methods=['GET'])
def get_drivers():
    return jsonify(drivers)

@app.route('/api/drivers/<int:driver_id>', methods=['GET'])
def get_driver(driver_id):
    driver = next((driver for driver in drivers if driver['id'] == driver_id), None)
    if driver is None:
        return jsonify({"message": "Driver not found"}), 404
    return jsonify(driver)

@app.route('/api/drivers', methods=['POST'])
def add_driver():
    new_driver = request.get_json()
    drivers.append(new_driver)
    return jsonify(new_driver), 201

@app.route('/api/drivers/<int:driver_id>', methods=['PATCH'])
def update_driver(driver_id):
    driver = next((driver for driver in drivers if driver['id'] == driver_id), None)
    if driver is None:
        return jsonify({"message": "Driver not found"}), 404
    updates = request.get_json()
    if 'wins' in updates:
        driver['wins'] += updates['wins']
    if 'poles' in updates:
        driver['poles'] += updates['poles']
    return jsonify(driver)

@app.route('/api/drivers/<int:driver_id>', methods=['DELETE'])
def delete_driver(driver_id):
    global drivers
    drivers = [driver for driver in drivers if driver['id'] != driver_id]
    return jsonify({"message": "Driver deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)