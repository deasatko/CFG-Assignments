from flask import Flask, jsonify, request  # Import necessary modules from Flask
from db_utils import get_users, get_watchlist, add_movie_to_watchlist, remove_movie_from_watchlist  # Import database functions
app = Flask(__name__)  # Create Flask application instance

@app.route("/")  # Define route for root endpoint
def hello_world():
    get_users()  # Call function to fetch users (prints to console)
    return "<p>Hello, World!</p>"  # Return HTML response

@app.route("/health")  # Define route for health endpoint
def health_endpoint():
    return jsonify(status="OK")  # Return JSON response indicating server health status

@app.route("/watchlist/<user_id>", methods=['GET'])  # Define route for retrieving watchlist of a user
def watchlist(user_id):
    if request.method == 'GET':  # If HTTP GET request is received
        return jsonify(get_watchlist(user_id))  # Return JSON response with user's watchlist
    else:
        return jsonify(error="Method not supported")  # Return error JSON response for unsupported methods

@app.route("/user/<user_id>/watchlist/<movie_id>", methods=['POST', 'DELETE'])  # Define route for adding or deleting movie from watchlist
def watchlist_handler(user_id, movie_id):
    if request.method == 'POST':  # If HTTP POST request is received
        add_movie_to_watchlist(user_id, movie_id)  # Call function to add movie to user's watchlist
        return jsonify(result="Success")  # Return success JSON response
    elif request.method == 'DELETE':  # If HTTP DELETE request is received
        try:
            remove_movie_from_watchlist(user_id, movie_id)  # Call function to remove movie from user's watchlist
            return jsonify(result="Success")  # Return success JSON response
        except:
            return jsonify(error="Could not remove from watchlist")  # Return error JSON response if removal fails
