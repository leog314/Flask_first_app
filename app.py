from flask import *
import flask_sqlalchemy as sql
import numpy as np

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
app.secret_key = b'[#h:H\xa7/\x81\xf4\xc4\xc7\xc5\x16\x90\x921\x10\xac\xc7:\xaa\xf6}\x01'
app.name = "Application"
db = sql.SQLAlchemy(app)


class user(db.Model):
    user = db.Column(db.String(200), primary_key = True)
    email = db.Column(db.String(200))
    password = db.Column(db.String(500))


with app.app_context():
    db.create_all()


@app.route("/", methods=["POST", "GET"])
def main_page():
    if request.method == "POST":
        if "search" == request.form["name"]:
            print("ok")
    return render_template("main_page.html", guess="")#float(model.forward(np.array([[1920], [-1919]]))))


@app.route("/login", methods=["POST", "GET"])
def login():
    error = "example@gmail.com"
    if "login" in request.form:
        email = request.form.get("email")
        passw = request.form.get("passw")
        try:
            rpass = db.get_or_404("password", email)
            if passw == rpass:
                return redirect("/")
            else:
                error = "Unknown user!"
        except:
            error = "Unknown user!"
    return render_template("login.html", error=error)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    error = "example@gmail.com"
    if request.method == "GET":
        if "signup" in request.form:
            return render_template("main_page.html")
    return render_template("signup.html", error=error)


if __name__ == "__main__":
    app.run()
