from flask import Flask, request, jsonify

app = Flask(__name__)

# Initial Data
users = [
    {"id": 1, "name": "Raja"},
    {"id": 2, "name": "Rama"}
]

@app.route("/", methods=["GET"])
def home():
    return "Welcome"

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"message": "user not found"}), 404

@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    new_user = {
        "id": len(users) + 1,
        "name": data.get("name")
    }
    users.append(new_user)
    return jsonify(new_user), 201

# Endpoint for Full Update
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name")
            return jsonify(user)
    return jsonify({"message": "user not found"}), 404

# Endpoint for Partial Update (Renamed to avoid the error)
@app.route("/users/<int:user_id>", methods=["PATCH"])
def patch_user(user_id):
    data = request.json
    for user in users:
        if user["id"] == user_id:
            # Only update the name if it's provided in the JSON body
            if "name" in data:
                user["name"] = data.get("name")
            return jsonify(user)
    return jsonify({"message": "user not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)