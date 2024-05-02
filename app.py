from flask import Flask, render_template, request #flask import
from random import randrange
import mariadb
import sys

try:
    conn = mariadb.connect(
        user="d3xj7d753lhx14ad",
        password="qyjau9ud4manbl1w",
        host="z12itfj4c1vgopf8.cbetxkdyhwsb.us-east-1.rds.amazonaws.com",
        port=3306,
        database="nodabg0vdbkgxoop"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB platform: {e}")
    sys.exit(1)

db = conn.cursor(dictionary=True)

app = Flask(__name__) # to initiate this for web app

@app.route("/")
def index():
    db.execute("SELECT * FROM hellos;")
    rows = db.fetchall()
    randindex = randrange(len(rows))

    return render_template("index.html", status = rows[randindex]['message'])
