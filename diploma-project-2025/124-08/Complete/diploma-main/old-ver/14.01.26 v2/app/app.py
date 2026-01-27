from flask import Flask, render_template_string
import os
import time
import mysql.connector
from datetime import datetime

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "app")
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppass")
DB_NAME = os.getenv("DB_NAME", "appdb")
IMAGE_TAG = os.getenv("IMAGE_TAG", "unknown")


def wait_for_db():
    for i in range(30):
        try:
            return mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
            )
        except Exception:
            time.sleep(2)
    raise RuntimeError("Database not ready")


def init_db_and_log_deploy():
    conn = wait_for_db()
    cur = conn.cursor()

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

    conn.commit()
    cur.close()
    conn.close()


@app.route("/")
def index():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cur = conn.cursor()
    cur.execute("SELECT id, deployed_at, image_tag FROM deployments ORDER BY id DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return render_template_string("""
        <h1>Deploy history</h1>
        <p>Current IMAGE_TAG: <b>{{ tag }}</b></p>
        <ul>
        {% for r in rows %}
          <li>#{{ r[0] }} | {{ r[1] }} | {{ r[2] }}</li>
        {% endfor %}
        </ul>
    """, rows=rows, tag=IMAGE_TAG)


if __name__ == "__main__":
    init_db_and_log_deploy()
    app.run(host="0.0.0.0", port=5000)
