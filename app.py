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
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#DB Models

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)

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
@app.route("/login", methods=["POST"])
def login():
    # Collect info from the form
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        return render_template("index.html")


#Register
@app.route("/register", methods = ["POST"])
def register():
    username = request.form['username']
    password = request.form['password']
    # input validation
    if not username or not password:
        return render_template("index.html", error="Please fill in all the fields")
    
    user = User.query.filter_by(username=username).first()
    if user:
        return render_template("index.html", error="Username exists")
    
    #Create new user
    else:
        new_user= User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        # Store session data (log in the user after registration)
        session['username'] = username
        return redirect(url_for('dashboard'))

#Dashboard
@app.route("/dashboard")
def dashboard():
    if "username" in session:
        return render_template('dashboard.html', username = session['username'])
    
    else:
        return redirect(url_for('home'))

#Logout
@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)