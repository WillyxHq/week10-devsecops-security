from flask import Flask, request
import hashlib
import os
import subprocess
import random
import pickle

AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
GITHUB_PAT = os.getenv("GITHUB_PAT")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

app = Flask(__name__)

# -------------------------
# Vulnerability 1
# Hardcoded Secret
# -------------------------
API_KEY = "sk_test_1234567890abcdef"

# -------------------------
# Vulnerability 2
# Hardcoded Password
# -------------------------
DB_PASSWORD = "Password123"


@app.route("/")
def home():
    return "Week 10 DevSecOps Vulnerable Flask App"


# -------------------------
# Vulnerability 3
# MD5 Hashing
# -------------------------
@app.route("/hash")
def weak_hash():

    text = request.args.get("text", "hello")
    return hashlib.md5(text.encode()).hexdigest()


# -------------------------
# Vulnerability 4
# os.system()
# -------------------------
@app.route("/ping")
def ping():

    host = request.args.get("host", "127.0.0.1")

    os.system("ping -c 1 " + host)

    return "Ping executed"


# -------------------------
# Vulnerability 5
# subprocess(shell=True)
# -------------------------
@app.route("/list")
def files():

    directory = request.args.get("dir", ".")

    subprocess.call("ls " + directory, shell=True)

    return "Directory Listed"


# -------------------------
# Vulnerability 6
# eval()
# -------------------------
@app.route("/calc")
def calc():

    expression = request.args.get("exp")

    return str(eval(expression))


# -------------------------
# Vulnerability 7
# pickle.loads()
# -------------------------
@app.route("/pickle", methods=["POST"])
def deserialize():

    data = request.data

    obj = pickle.loads(data)

    return str(obj)


# -------------------------
# Vulnerability 8
# Weak Random
# -------------------------
@app.route("/token")
def token():

    return str(random.random())


if __name__ == "__main__":
    app.run(debug=True)
