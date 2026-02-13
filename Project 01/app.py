from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary data storage (In-memory database)
restaurants = []


# 1. Register a Restaurant (Requirement #1)
@app.route('/api/v1/restaurants', methods=['POST'])
def register_restaurant():
    data = request.get_json()
    # Basic validation
    if not data or 'name' not in data:
        return jsonify({"message": "Bad Request"}), 400

    restaurants.append(data)
    return jsonify(data), 201


# 2. Get All Restaurants (Requirement #4)
@app.route('/api/v1/restaurants', methods=['GET'])
def get_restaurants():
    return jsonify(restaurants), 200


# 3. Update Restaurant (Requirement #2)
@app.route('/api/v1/restaurants/<string:name>', methods=['PUT'])
def update_restaurant(name):
    data = request.get_json()
    for res in restaurants:
        if res['name'] == name:
            res.update(data)
            return jsonify(res), 200
    return jsonify({"message": "Not Found"}), 404


# 4. Delete Restaurant (Requirement #3)
@app.route('/api/v1/restaurants/<string:name>', methods=['DELETE'])
def delete_restaurant(name):
    global restaurants
    restaurants = [res for res in restaurants if res['name'] != name]
    return jsonify({"message": "Restaurant Deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)