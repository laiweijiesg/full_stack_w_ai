# Imports
from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import func

# App 
app = Flask(__name__)
Scss(app)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

# initialize the app with the extension
db = SQLAlchemy(app)


# Data Class ~ Row of data
class MyTask(db.Model): 

    # Unique ID
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(100), nullable = False)
    complete = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=func.now())




# Routes
@app.route("/")
def index():
    return render_template("index.html")




if __name__ in "__main__":
    app.run(debug=True)