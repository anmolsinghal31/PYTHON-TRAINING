from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data (Example list of users)
users = [
    {"id": 1, "name": "Anmol"},
    {"id": 2, "name": "Rahul"}
]


@app.route("/users/<int:user_id>", methods=["PATCH"])
def patch_user(user_id):
    data = request.json
    for user in users:
        if user["id"] == user_id:
            if "name" in data:
                user["name"] = data["name"]
            return jsonify(user), 200

    return jsonify({"message": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)