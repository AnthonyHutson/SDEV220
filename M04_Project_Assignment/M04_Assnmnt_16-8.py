"""Programming Assignment 16.8
   Anthony Hutson
   11/17/2024"""

import sqlite3
conn = sqlite3.connect('books.db')
curs = conn.cursor()
ins = "INSERT INTO books (title, author, year) VALUES(?, ?, ?)"
curs.execute(ins, ('The Weirdstone of Brisingamen', 'Alan Garner', 1960))
curs.execute(ins, ('Perdido Street Station', 'China Mieville', 2000))
curs.execute(ins, ('Thud!', 'Terry Pratchett', 2005))
curs.execute(ins, ('The Spellman Files', 'Lisa Lutz', 2007))
curs.execute(ins, ('Small Gods', 'Terry Pratchett', 1992))
conn.commit()
curs.close()
conn.close()