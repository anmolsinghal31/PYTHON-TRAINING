from flask import Flask, request, jsonify

app = Flask(__name__)

restaurants = []
dishes = []
users = []
orders = []
admin_approvals = []

@app.route('/api/v1/restaurants', methods=['POST'])
def register_restaurant():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"message": "Bad Request"}), 400
    restaurants.append(data)
    return jsonify(data), 201

@app.route('/api/v1/restaurants', methods=['GET'])
def get_restaurants():
    return jsonify(restaurants), 200

@app.route('/api/v1/dishes', methods=['POST'])
def add_dish():
    data = request.get_json()
    if not data or 'dish_name' not in data:
        return jsonify({"message": "Invalid Dish Data"}), 400
    dishes.append(data)
    return jsonify({"message": "Dish added successfully", "dish": data}), 201

@app.route('/api/v1/dishes', methods=['GET'])
def get_all_dishes():
    return jsonify(dishes), 200

@app.route('/api/v1/admin/approve', methods=['POST'])
def approve_restaurant():
    data = request.get_json()
    admin_approvals.append(data)
    return jsonify({"status": "Success", "message": "Restaurant Approved by Admin"}), 200

@app.route('/api/v1/users', methods=['POST'])
def register_user():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"message": "Registration Failed"}), 400
    users.append(data)
    return jsonify({"message": "User Account Created", "user": data}), 201

@app.route('/api/v1/orders', methods=['POST'])
def place_order():
    data = request.get_json()
    orders.append(data)
    return jsonify({"message": "Order Placed Successfully", "order_details": data}), 201

@app.route('/api/v1/orders', methods=['GET'])
def get_orders():
    return jsonify(orders), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)