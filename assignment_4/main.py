import requests  # Importing the requests library for making HTTP requests
import argparse  # Importing argparse for parsing command-line arguments

BASE_URL = "http://127.0.0.1:5000"  # Base URL of the Flask server

def hello_world():
    response = requests.get(f"{BASE_URL}/")  # Sending a GET request to the root endpoint
    if response.status_code == 200:
        print(response.text)  # Printing the response text if request is successful (status code 200)
    else:
        print("Failed to fetch hello world message")  # Printing a message if request fails

def check_health():
    response = requests.get(f"{BASE_URL}/health")  # Sending a GET request to the health endpoint
    if response.status_code == 200:
        print(response.json())  # Printing the JSON response if request is successful (status code 200)
    else:
        print("Health check failed")  # Printing a message if request fails

def get_watchlist(user_id):
    response = requests.get(f"{BASE_URL}/watchlist/{user_id}")  # Sending a GET request to fetch user's watchlist
    if response.status_code == 200:
        print(response.json())  # Printing the JSON response of the watchlist if request is successful (status code 200)
    else:
        print("Failed to fetch watchlist")  # Printing a message if request fails

def add_to_watchlist(user_id, movie_id):
    response = requests.post(f"{BASE_URL}/user/{user_id}/watchlist/{movie_id}")  # Sending a POST request to add movie to user's watchlist
    if response.status_code == 200:
        print(response.json())  # Printing the JSON response if request is successful (status code 200)
    else:
        print("Failed to add movie to watchlist")  # Printing a message if request fails

def remove_from_watchlist(user_id, movie_id):
    response = requests.delete(f"{BASE_URL}/user/{user_id}/watchlist/{movie_id}")  # Sending a DELETE request to remove movie from user's watchlist
    if response.status_code == 200:
        print(response.json())  # Printing the JSON response if request is successful (status code 200)
    else:
        print("Failed to remove movie from watchlist")  # Printing a message if request fails

def main():
    parser = argparse.ArgumentParser(description="CLI client for Flask app")  # Creating an ArgumentParser object
    parser.add_argument("action", choices=["hello", "health", "watchlist", "add", "delete"], help="Action to perform")  # Adding positional argument for action
    parser.add_argument("--user_id", type=str, help="User ID")  # Adding optional argument for user ID
    parser.add_argument("--movie_id", type=str, help="Movie ID")  # Adding optional argument for movie ID

    args = parser.parse_args()  # Parsing command-line arguments

    if args.action == "hello":
        hello_world()  # Calling hello_world function if action is 'hello'
    elif args.action == "health":
        check_health()  # Calling check_health function if action is 'health'
    elif args.action == "watchlist":
        if args.user_id:
            get_watchlist(args.user_id)  # Calling get_watchlist function with user ID if action is 'watchlist'
        else:
            print("User ID is required for fetching watchlist")  # Printing error message if user ID is not provided
    elif args.action == "add":
        if args.user_id and args.movie_id:
            add_to_watchlist(args.user_id, args.movie_id)  # Calling add_to_watchlist function with user ID and movie ID if action is 'add'
        else:
            print("User ID and Movie ID are required for adding to watchlist")  # Printing error message if user ID or movie ID is missing
    elif args.action == "delete":
        if args.user_id and args.movie_id:
            remove_from_watchlist(args.user_id, args.movie_id)  # Calling remove_from_watchlist function with user ID and movie ID if action is 'delete'
        else:
            print("User ID and Movie ID are required for deleting from watchlist")  # Printing error message if user ID or movie ID is missing

if __name__ == "__main__":
    main()  # Calling main function if script is executed directly
