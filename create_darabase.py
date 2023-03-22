import sqlite3

conn = sqlite3.connect('highscore.db')
query = (''' CREATE TABLE HIGH_SCORE
            (NAME TEXT NOT NULL,
            SCORE INT);''')
conn.execute(query)
conn.close()