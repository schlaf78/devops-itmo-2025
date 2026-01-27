from flask import Flask, render_template
import os
import mysql.connector
from datetime import datetime
import time

app = Flask(__name__)

IMAGE_TAG = os.getenv("IMAGE_TAG", "unknown")

DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "app")
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppass")
DB_NAME = os.getenv("DB_NAME", "appdb")


def db_conn():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )


def init_db_and_log_deploy():
    # ждём БД и делаем запись о деплое ОДИН РАЗ при старте контейнера
    for _ in range(30):
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

            cur.execute(
                "INSERT INTO deployments (deployed_at, image_tag) VALUES (%s, %s)",
                (datetime.utcnow(), IMAGE_TAG)
            )

            c.commit()
            cur.close()
            c.close()
            return
        except Exception:
            time.sleep(2)

    raise Exception("DB not ready")


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
    init_db_and_log_deploy()
    app.run(host="0.0.0.0", port=5000)
