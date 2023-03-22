import sqlite3

def insert_contact(name, score):
    conn = sqlite3.connect('highscore.db')
    conn.execute("INSERT INTO HIGH_SCORE (NAME,SCORE ) \
VALUES (?,?)", (name,score))
    conn.commit()
    conn.close()


def retrieve_contacts():
    results = []
    conn = sqlite3.connect('highscore.db')
    cursor = conn.execute("SELECT name, score from HIGH_SCORE")
    # Contact records are tuples and need to be converted into an array
    for row in cursor:
        results.append(list(row))
    return results