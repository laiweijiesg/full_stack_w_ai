# Imports
from flask import Flask, render_template, redirect, request
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

    def __repr__(self):
        return f"Task {self.id}"




# Routes
@app.route("/", methods = ["POST", "GET"])
def index():
    # Add a task
    if request.method == "POST":
        current_task = request.form['content']
        new_task = MyTask(content=current_task)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        
        except Exception as e:
            print(f"Error:{e}")
            return f"Error:{e}"

    # See all tasks
    else: 
        tasks = MyTask.query.order_by(MyTask.created).all()
        return render_template("index.html", tasks=tasks)






if __name__ in "__main__":
    app.run(debug=True)