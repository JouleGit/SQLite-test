import flask
import sqlite3
from flask import request


app = flask.Flask(__name__)
app.config["DEBUG"] = True # Enable debug mode to enable hot-reloader.


@app.route('/tutorial', methods=['GET'])
def tutorial():
    name = request.args.get('name', '')

    con = sqlite3.connect('my-db.db')
    
    # insert into db
    if len(name) > 0:
     
        insertQuery = "INSERT INTO STUDENT (NAME) values (?);"
        con.execute(insertQuery, (name,))
        con.commit()
        
    # Getting info from db
    cursor = con.execute("SELECT NAME from STUDENT;") 
    students = []
    for row in cursor:
        students.append(row[0])
    con.close()
    
    outdata = {
    "course_code": "COMP3330",
    "course_name": "Interactive Mobile Application Design and Programming",
    "teachers": ["Dr. T.W. Chim", "Mr. C.K. Lai", "Mr. X. Wang"],
    "students": students
    }
    return outdata

@app.route('/')
def Hello():
    return "Hello Guys"


# adds host="0.0.0.0" to make the server publicly available
app.run(host="0.0.0.0")
