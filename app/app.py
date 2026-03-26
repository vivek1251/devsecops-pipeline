# DevSecOps Pipeline v2 - Security scanning active
from flask import Flask, request
from flask_wtf.csrf import CSRFProtect
import sqlite3
import os

app = Flask(__name__)

# Secrets loaded from environment variables (not hardcoded)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback-dev-key')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')

# CSRF Protection enabled
csrf = CSRFProtect(app)

def get_db():
    conn = sqlite3.connect("users.db")
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, password TEXT)")
    return conn

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

@app.route("/search")
def search():
    # Intentional vulnerability 2: SQL Injection
    name = request.args.get("name", "")
    conn = get_db()
    query = f"SELECT * FROM users WHERE name = '{name}'"
    result = conn.execute(query).fetchall()
    return {"result": str(result)}, 200

@app.route("/user")
def user():
    # Intentional vulnerability 3: Command injection
    username = request.args.get("username", "")
    os.system(f"echo {username}")
    return {"user": username}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)