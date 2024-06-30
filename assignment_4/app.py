from flask import Flask, jsonify, request
from db_utils import get_users, get_watchlist, add_movie_to_watchlist
app = Flask(__name__)

@app.route("/")
def hello_world():
    get_users()
    return "<p>Hello, World!</p>"

#adding additional enpoint (GET request)
@app.route("/health")
def health_endpoint():
    return jsonify(status = "OK")

@app.route("/watchlist/<user_id>", methods = ['GET'])
def watchlist(user_id):
    if request.method == 'GET':
        return jsonify(get_watchlist(user_id))
    else:
        return jsonify(error = "Method not supported")
    
@app.route("/user/<user_id>/watchlist/<movie_id>", methods = ['POST', 'DELETE'])
def watchlist_handler(user_id, movie_id):
    if request.method == 'POST':
        try:
            add_movie_to_watchlist(user_id, movie_id)
            return jsonify(result = "Success" )
        except:
            return jsonify(error = "Could not add to watchlist")