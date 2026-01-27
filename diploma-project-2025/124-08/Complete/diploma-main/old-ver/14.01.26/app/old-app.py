from flask import Flask, render_template
import os
import mysql.connector
import datetime
import time

app = Flask(__name__)

IMAGE_TAG = os.getenv("IMAGE_TAG", "unknown")

def db_conn():
    return mysql.connector.connect(
        host="db",
        user="app",
        password="apppass",
        database="appdb"
    )

def init_db():
    for _ in range(15):
        try:
            c = db_conn()
            cur = c.cursor()
            cur.execute("""
              CREATE TABLE IF NOT EXISTS deployments (
                id INT AUTO_INCREMENT PRIMARY KEY,
                deployed_at DATETIME NOT NULL,
                image_tag VARCHAR(64) NOT NULL
              )
            """)
            c.commit()
            cur.close()
            c.close()
            return
        except:
            time.sleep(2)
    raise Exception("DB not ready")

@app.before_first_request
def register_deploy():
    # Это выполнится при первом запросе (проще, чем ловить старт)
    c = db_conn()
    cur = c.cursor()
    cur.execute(
        "INSERT INTO deployments (deployed_at, image_tag) VALUES (%s, %s)",
        (datetime.datetime.now(), IMAGE_TAG)
    )
    c.commit()
    cur.close()
    c.close()

@app.route("/")
def index():
    c = db_conn()
    cur = c.cursor()
    cur.execute("SELECT id, deployed_at, image_tag FROM deployments ORDER BY id DESC")
    rows = cur.fetchall()
    cur.close()
    c.close()

    return render_template("index.html", rows=rows, image_tag=IMAGE_TAG)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
