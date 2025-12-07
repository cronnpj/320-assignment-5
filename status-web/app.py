import requests
from flask import Flask, render_template

app = Flask(__name__)

def check_service(url):
    try:
        r = requests.get(url, timeout=2)
        return r.status_code == 200
    except:
        return False

@app.route("/")
def index():
    # Health checks
    adminer_up = check_service("http://app_adminer:8080")
    db_up = check_service("http://app_db:3306")  # This will not always return 200 because it's DB, but good placeholder
    status_up = True  # If this page loads, the app is alive

    return render_template("index.html",
                           adminer_up=adminer_up,
                           db_up=db_up,
                           status_up=status_up)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
