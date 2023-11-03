import sqlite3
# Connects to database
# The .db file is created automatically if it does not exist
con = sqlite3.connect('my-db.db')
# Creates table
con.execute("""CREATE TABLE IF NOT EXISTS STUDENT (
 ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
 NAME TEXT NOT NULL,
 CREATE_TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP
 );""")
# insert test data
testData = ['Anthony', 'Ben', 'John', 'Kenneth', 'Loretta']
for name in testData:
 insertQuery = "INSERT INTO STUDENT (NAME) values (?);"
 con.execute(insertQuery, (name,))
con.commit()
con.close()
