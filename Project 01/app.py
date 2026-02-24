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
    items = data.get('items', [])

    base_price = 0
    for item in items:
        base_price += item.get('price', 0) * item.get('quantity', 1)

    gst = base_price * 0.05
    delivery_charge = 40.0
    total_bill = base_price + gst + delivery_charge

    order_details = {
        "order_id": len(orders) + 1,
        "items": items,
        "base_price": base_price,
        "gst_amount": gst,
        "delivery_charge": delivery_charge,
        "total_bill": total_bill
    }

    orders.append(order_details)
    return jsonify({"message": "Order Placed Successfully", "bill": order_details}), 201


@app.route('/api/v1/orders', methods=['GET'])
def get_orders():
    return jsonify(orders), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)