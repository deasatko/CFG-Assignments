import mysql.connector  # Import MySQL Connector Python module.
from config import USER, PASSWORD, HOST, DATABASE  # Import credentials from config file.

class DbConnectionError(Exception):  # Define custom exception for database connection errors.
    pass

# Function that connects to my server in SQL
def _connect_to_db():
    cnx = mysql.connector.connect(  # Establish connection to MySQL database.
        host=HOST,  # Set host from config.
        user=USER,  # Set user from config.
        password=PASSWORD,  # Set password from config.
        auth_plugin='mysql_native_password',  # Use native password authentication.
        database=DATABASE  # Set database name from config.
    )
    return cnx  # Return the connection object.

# Funcion that gets all users from my database.
def get_users():
    connection = _connect_to_db()  # Connect to the database.
    mycursor = connection.cursor()  # Create a cursor object to interact with the database.

    mycursor.execute("SELECT * FROM user")  # Execute SQL query to fetch all users.

    myresult = mycursor.fetchall()  # Fetch all rows from the result set.

    for x in myresult:  # Iterate through results and print each row.
       print(x)  # Print each row to the terminal for testing.

# Function that gets all movies from the user X that were added to the watchlist.        
def get_watchlist(user_id):
    connection = _connect_to_db()  # Connect to the database.
    try:
        mycursor = connection.cursor()  # Create a cursor object to interact with the database.
    
        query = """SELECT title, release_year, genre FROM movie JOIN watchlist ON watchlist.movie_id = movie.id WHERE watchlist.user_id = '{}'""".format(user_id)  # Construct SQL query to fetch movies in the user's watchlist.
        mycursor.execute(query)  # Execute the SQL query.

        result = mycursor.fetchall()  # Fetch all rows from the result set.
        return result  # Return the fetched results.
    except:
        return []  # Return an empty list if there's an exception.#
    finally:
        connection.close()

# Function that adds movies from user to watchlist when the user queries it.    
def add_movie_to_watchlist(user_id, movie_id):
    connection = _connect_to_db()  # Connect to the database.
    try:
        mycursor = connection.cursor()  # Create a cursor object to interact with the database.
    
        query = "INSERT INTO watchlist (user_id, movie_id) VALUES(%s,%s)"  # Construct SQL query to insert movie into watchlist.
        mycursor.execute(query,(user_id,movie_id))  # Execute the SQL query with user_id and movie_id values.
        connection.commit()  # Commit to the database.
    except:
        raise Exception("Could not add to watchlist")  # Raise an exception if insertion fails.
    finally:
        connection.close()

def remove_movie_from_watchlist(user_id, movie_id):
    connection = _connect_to_db()  # Connect to the database.
    try:
        mycursor = connection.cursor()  # Create a cursor object to interact with the database.
        
        query = "DELETE FROM watchlist WHERE user_id = %s AND movie_id = %s"  # Construct SQL query to delete movie from watchlist.
        mycursor.execute(query, (user_id, movie_id))  # Execute the SQL query with user_id and movie_id values.
        connection.commit()  # Commit the transaction to the database.
    except mysql.connector.Error as err:
        print(f"Error: {err}")  # Print error message if there's a MySQL-specific error.
        raise  # Re-raise the exception.
    finally:
        connection.close()  # Close the database connection.
