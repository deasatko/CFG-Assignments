import mysql.connector
from config import USER, PASSWORD, HOST, DATABASE

class DbConnectionError(Exception):
    pass


def _connect_to_db():
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=DATABASE
    )
    return cnx

def get_users():
    connection = _connect_to_db()
    mycursor = connection.cursor()

    mycursor.execute("SELECT * FROM user")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
        
def get_watchlist(user_id):
    connection = _connect_to_db()
    try:
        mycursor = connection.cursor()
    
        query = """SELECT title, release_year, genre FROM movie JOIN watchlist ON watchlist.movie_id = movie.id WHERE watchlist.user_id = '{}'""".format(user_id)  
        mycursor.execute(query)
        result = mycursor.fetchall()
        return result
    except:
        return []
    
def add_movie_to_watchlist(user_id, movie_id):
    connection = _connect_to_db()
    try:
        mycursor = connection.cursor()
    
        query = "INSERT INTO watchlist (user_id, movie_id) VALUES(%s,%s)"
        mycursor.execute(query,(user_id,movie_id))
        connection.commit()
    except:
        raise Exception("Could not add to watchlist")
    