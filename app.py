from flask import Flask, render_template, request #flask import
import mariadb
import sys

try:
    conn = mariadb.connect(
        user="andre",
        password="password",
        host="localhost",
        port=3306,
        database="helloDB"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB platform: {e}")
    sys.exit(1)

db = conn.cursor(dictionary=True)

app = Flask(__name__) # to initiate this for web app

@app.route("/")
def index():
    rows = db.execute("SELECT * FROM hellos;")
    rows = db.fetchall()

    print(f"show DBs : {rows}")
    return render_template("index.html", status = rows[1]['message'])
