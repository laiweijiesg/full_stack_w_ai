from flask import Flask, render_template, request,redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "key"

Scss(app)

#SQL Config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)

#DB Models
class Todo(db.Model):
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(25), unique=True, nullable=False)
        password = db.Column(db.String(150), nullable=False)

        def set_password(self, password):
            self.password_hash = generate_password_hash(password)

        def check_password(self, password):
            return check_password_hash(self.password_hash, password)
    
with app.app_context():
    db.create_all()

#Routes
@app.route("/")
def home():
    if "username" in session: #if user loged in, go to user dash, otherwise go to home screen
        return redirect(url_for('dashboard'))
    
    return render_template("index.html")

#Login

#Register


#Dashboard


if __name__ == "__main__":
    app.run(debug=True)