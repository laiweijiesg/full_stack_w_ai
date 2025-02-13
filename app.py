from flask import Flask, render_template, request,redirect
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
Scss(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    """A Model for an Item in the Todo List

    Args:
        db (_type_): database model

    Returns:
        __repr__: string rep.
    """
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime)
    
    def __repr__(self):
        return f'Task {self.id}'
    
with app.app_context():
    db.create_all()
    


@app.route('/', methods=["POST","GET"])

def index():
    """Main page for App

    Returns:
        page: home page
    """
    if request.method == "POST":
        task_content = request.form['content']
        due_date_str = request.form['due_date'] #Get due date from form
        due_date = datetime.strptime(due_date_str, '%Y-%m-%dT%H:%M') if due_date_str else None  # Convert string to datetime

        new_task = Todo(content=task_content, due_date=due_date)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"Error:{e}")
            return f'Error:{e}'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html',tasks=tasks)

@app.route("/delete/<int:id>")
def delete(id):
    """delete an item from the todo list

    Args:
        id (int): uuid for each item in the todo list

    Returns:
        redirect: delete and return to home
    """
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()  
        return redirect("/")
    except Exception as e:
        return f"Error:{e}"

@app.route("/update/<int:id>", methods=["GET","POST"])
def update(id):
    """update an item from the todo list

    Args:
        id (int): uuid for each item in the todo list

    Returns:
        redirect: update and return to home
    """
    task = Todo.query.get_or_404(id)
    
    if request.method == "POST":
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"ERROR:{e}")
            return "Error"
    else:
        return render_template("update.html", task=task)

@app.route("/update_due/<int:id>", methods=["GET", "POST"])

def update_due(id):
    """Update only the due date of a task."""
    task = Todo.query.get_or_404(id)

    if request.method == "POST":
        due_date_str = request.form["due_date"]
        task.due_date = datetime.strptime(due_date_str, "%Y-%m-%dT%H:%M") if due_date_str else None

        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"ERROR: {e}")
            return "Error updating due date"
    else:
        return render_template("update_due.html", task=task)


if __name__ == "__main__":
    app.run(debug=True)