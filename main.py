from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database of users
users = {
    "1": {"id": 1, "name": "John Doe", "age": 30},
    "2": {"id": 2, "name": "Jane Smith", "age": 25},
    "3": {"id": 3, "name": "Alice Johnson", "age": 35},
}

@app.route("/get-user/<user_id>")
def get_user(user_id):
    # Check if the user exists in the mock database
    user_data = users.get(user_id)
    
    if not user_data:
        return jsonify({"error": "User not found"}), 404

    # Optionally add extra data from query parameters
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

if __name__ == '__main__':
    app.run(debug=True)