"""Programming Assignment 16.8
   Anthony Hutson
   11/17/2024"""

import sqlite3 as sq

conn = sq.connect('books.db')
curs = conn.cursor()
curs.execute("SELECT title from books ORDER BY title")
result = curs.fetchall()
print(result)