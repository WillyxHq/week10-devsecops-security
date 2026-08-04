from flask import Flask, request
import hashlib
import os
import subprocess
import secrets
import json

AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
GITHUB_PAT = os.getenv("GITHUB_PAT")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

app = Flask(__name__)

# -------------------------
# Vulnerability 1
# Hardcoded Secret
# -------------------------
API_KEY = os.getenv("API_KEY")

# -------------------------
# Vulnerability 2
# Hardcoded Password
# -------------------------
DB_PASSWORD = os.getenv("DB_PASSWORD")


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
    return hashlib.sha256(text.encode()).hexdigest()


# -------------------------
# Vulnerability 4
# os.system()
# -------------------------
@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")

    subprocess.run(
        ["ping", "-c", "1", host],
    	check=True,
    	shell=False
)

    return "Ping executed"


# -------------------------
# Vulnerability 5
# subprocess(shell=True)
# -------------------------
@app.route("/list")
def files():

    directory = request.args.get("dir", ".")
   
    subprocess.run(
        ["ls", directory],
        check=True,
        shell=False,
        capture_output=True,
        text=True
    )

    return "Directory Listed"


# -------------------------
# Vulnerability 6
# eval()
# -------------------------
@app.route("/calc")
def calc():

	return "Expression evaluation has been disabled for security reasons."

# -------------------------
# Vulnerability 7
# pickle.loads()
# -------------------------
@app.route("/deserialize", methods=["POST"])
def deserialize():
    data = request.get_json()

    if data is None:
        return "Invalid JSON", 400
 
    return str(data)


# -------------------------
# Vulnerability 8
# Weak Random
# -------------------------
@app.route("/token")
def token():

    return secrets.token_hex(16)


if __name__ == "__main__":
    app.run(debug=False)
