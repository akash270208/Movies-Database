import sqlite3  ## sqlite library # database

from functools import reduce

connection = sqlite3.connect('movie.db')
# print("Database opened successfully")

TABLE_NAME = "movie_table"
MOVIE_ID = "MOVIE_ID"
MOVIE_NAME = "MOVIE_NAME"
MOVIE_DURATION = "MOVIE_DURATION"
MOVIE__RELEASE = "MOVIE__RELEASE"
MOVIE_RATING = "MOVIE_RATING"
MOVIE_GENRE = "MOVIE_GENRE"
connection.execute(" CREATE TABLE IF NOT EXISTS "
                   + TABLE_NAME
                   + "( " + MOVIE_ID +
                   " INTEGER PRIMARY KEY " +
                   " AUTOINCREMENT, " +
                   MOVIE_NAME + " TEXT, " +
                   MOVIE_DURATION + " TEXT, " +
                   MOVIE__RELEASE + " INTEGER, " +
                   MOVIE_RATING + " REAL, " +
                   MOVIE_GENRE + " TEXT) ;")

def insert_into(name, duration, release, rating, genre):
    connection.execute("INSERT INTO " + TABLE_NAME +
                   "( " + MOVIE_NAME + ", "
                   + MOVIE_DURATION + ", " +
                   MOVIE__RELEASE + ", " + MOVIE_RATING + ", " +
                   MOVIE_GENRE +
                   ") VALUES(?,?,?,?,?);",
                   (name.upper(), duration.upper(), release, rating, genre.upper()))
    connection.commit()
    # connection.close()


def viewTableCursor():
    connection = sqlite3.connect('movie.db')
    TABLE_NAME = "movie_table"
    cursor = connection.execute("SELECT*FROM " + TABLE_NAME + " ;")
    return cursor

def colCount():
    connection = sqlite3.connect('movie.db')
    TABLE_NAME="movie_table"
    # count= connection.execute("SELECT COUNT(*) FROM " + TABLE_NAME + " ;")
    count = reduce(lambda x, y: x+y, connection.execute("SELECT * FROM " + TABLE_NAME + " ;"))
    return count

def delRec(del_id):
    connection=sqlite3.connect('movie.db')
    TABLE_NAME="movie_table"
    # count1 = colCount()
    count1=reduce(lambda x, y: x+y, connection.execute("SELECT * FROM " + TABLE_NAME + " ;"))
    connection.execute("DELETE FROM " + TABLE_NAME + " WHERE " + MOVIE_ID + " = ?", [del_id])
    connection.commit()
    # count2 = colCount()
    count2=reduce(lambda x, y: x+y, connection.execute("SELECT * FROM " + TABLE_NAME + " ;"))
    # connection.close()
    if(count1 != count2):
        return 1
    else:
        return 0
