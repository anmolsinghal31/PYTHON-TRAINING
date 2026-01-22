from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary data storage (List of dictionaries)
users = [
    {"id": 1, "name": "Gemini"},
    {"id": 2, "name": "Wipro Prep"}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.json
    # Assign a simple ID
    new_user['id'] = len(users) + 1
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    print("Server starting on http://127.0.0.1:5000...")
    app.run(port=5000, debug=True)