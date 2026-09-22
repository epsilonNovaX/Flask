from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    #data=request.get_json()
    #username=data.get("username")
    #password=data.get("password") only in case of JSON passing at frontend 
    username=request.form.get("username")
    password=request.form.get("password")
    print(username)
    print(password)
    return "DATA RECIEVED!"


if __name__ == "__main__":
    app.run(debug=True)