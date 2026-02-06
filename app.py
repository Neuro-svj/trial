
from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

DB_PATH = os.path.join(os.path.dirname(__file__), "db", "database.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def dashboard():
    db = get_db()
    metrics = db.execute("SELECT * FROM metrics ORDER BY collected_at DESC").fetchall()
    db.close()
    return render_template("dashboard.html", metrics=metrics)


if __name__ == "__main__":
    # Render injects PORT dynamically
    port = int(os.environ.get("PORT", 5000))

    # Bind to 0.0.0.0 so Render can expose it
    app.run(
        host="0.0.0.0",
        port=port,
        debug=False  # NEVER True in production
    )
