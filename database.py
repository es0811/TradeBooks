import psycopg2

#Connect to the database
def connect():
    conn = psycopg2.connect(
    host="localhost",
    database="bookworld",
    user="bookreader",
    password="books123")
    return conn
