from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Initial Data (In-memory storage)
movies = [
    {"id": 101, "movie_name": "Interstellar", "language": "English", "duration": "2h 49m", "price": 250},
    {"id": 102, "movie_name": "Inception", "language": "English", "duration": "2h 28m", "price": 200}
]
bookings = []


# --- Movie Routes ---

@app.route('/api/movies', methods=['GET'])
def get_movies():
    return jsonify(movies), 200


@app.route('/api/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = next((m for m in movies if m['id'] == movie_id), None)
    if movie is None:
        abort(404, description="Movie not found")
    return jsonify(movie), 200


@app.route('/api/movies', methods=['POST'])
def add_movie():
    if not request.json or 'movie_name' not in request.json:
        abort(400, description="Invalid request data")

    new_movie = {
        "id": movies[-1]['id'] + 1 if movies else 101,
        "movie_name": request.json['movie_name'],
        "language": request.json.get('language', "Unknown"),
        "duration": request.json.get('duration', "N/A"),
        "price": request.json.get('price', 0)
    }
    movies.append(new_movie)
    return jsonify(new_movie), 201


@app.route('/api/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    movie = next((m for m in movies if m['id'] == movie_id), None)
    if movie is None:
        abort(404)

    movie.update({
        "movie_name": request.json.get('movie_name', movie['movie_name']),
        "language": request.json.get('language', movie['language']),
        "duration": request.json.get('duration', movie['duration']),
        "price": request.json.get('price', movie['price'])
    })
    return jsonify(movie), 200


@app.route('/api/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    global movies
    movies = [m for m in movies if m['id'] != movie_id]
    return jsonify({"result": True}), 200


# --- Booking Routes ---

@app.route('/api/bookings', methods=['POST'])
def book_ticket():
    data = request.json
    movie_id = data.get('movie_id')

    # Validation
    movie_exists = any(m['id'] == movie_id for m in movies)
    if not movie_exists:
        return jsonify({"error": "Movie ID not found"}), 400

    booking = {
        "booking_id": len(bookings) + 1,
        "movie_id": movie_id,
        "seats": data.get('seats', 1)
    }
    bookings.append(booking)
    return jsonify(booking), 201


if __name__ == '__main__':
    app.run(debug=True, port=5000)