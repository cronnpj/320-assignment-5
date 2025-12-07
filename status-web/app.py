import requests
import socket
from flask import Flask, render_template

app = Flask(__name__)

# -----------------------------
# HTTP health check (Adminer)
# -----------------------------
def check_service(url):
    try:
        r = requests.get(url, timeout=2)
        return r.status_code == 200
    except:
        return False

# -----------------------------
# TCP health check (MariaDB)
# -----------------------------
def check_db(host, port):
    try:
        with socket.create_connection((host, port), timeout=2):
            return True
    except OSError:
        return False


# -----------------------------
# Main route
# -----------------------------
@app.route("/")
def index():

    # Status-Web is UP if we can render this page
    status_up = True

    # Adminer HTTP health check
    adminer_up = check_service("http://app_adminer:8080")

    # MariaDB TCP health check
    db_up = check_db("app_db", 3306)

    return render_template(
        "index.html",
        status_up=status_up,
        adminer_up=adminer_up,
        db_up=db_up
    )


# -----------------------------
# Flask entry point
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
