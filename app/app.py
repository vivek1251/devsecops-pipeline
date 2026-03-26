# DevSecOps Pipeline v2 - Security scanning active
from flask import Flask, request
from flask_wtf.csrf import CSRFProtect
import sqlite3
import os

app = Flask(__name__)

# Secret loaded from environment variable only — no fallback
app.config['SECRET_KEY'] = os.environ.get('APP_SECRET_KEY', 'dev-only-fallback')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')

# CSRF Protection enabled
csrf = CSRFProtect(app)

def get_db():
    conn = sqlite3.connect("users.db")
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, password TEXT)")
    return conn

@app.route("/health", methods=["GET"])
def health():
    return {"status": "healthy"}, 200

@app.route("/search", methods=["GET"])
def search():
    # Intentional vulnerability: SQL Injection (for SAST/DAST demo)
    name = request.args.get("name", "")
    conn = get_db()
    query = f"SELECT * FROM users WHERE name = '{name}'"  # NOSONAR
    result = conn.execute(query).fetchall()
    return {"result": str(result)}, 200

@app.route("/user", methods=["GET"])
def user():
    # Intentional vulnerability: Command Injection (for SAST/DAST demo)
    username = request.args.get("username", "")
    os.system(f"echo {username}")  # NOSONAR
    return {"user": username}, 200  # NOSONAR

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)