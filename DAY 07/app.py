from flask import Flask, jsonify, request

app = Flask(__name__)

# 4. Store data in an in-memory list
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]


# GET /users -> Return all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


# GET /users/<id> -> Return user details by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404


# POST /users -> Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    # Simple validation
    if not data or "name" not in data:
        return jsonify({"error": "Bad Request, 'name' is required"}), 400

    new_user = {
        "id": len(users) + 1,
        "name": data["name"]
    }
    users.append(new_user)

    # 3. Follow REST principles: Return 201 Created
    return jsonify(new_user), 201


if __name__ == '__main__':
    app.run(debug=True)

# DELETE /users/<id> -> Remove a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        users = [u for u in users if u["id"] != user_id]
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404