# full_stack_w_ai
Feb Project: Full Stack App w ML Component: Stock market (time series) or HDB Prices 

start : 11 Feb 2025 

youtube video for flask and deployment:
https://www.youtube.com/watch?v=45P3xQPaYxc&t=19s&ab_channel=CodewithJosh

intial deployment on:
pythonanywhere

URL: https://laiweijie88.pythonanywhere.com/

---

Day 1: 11 Feb 2025

Create venv:
python3 -m venv env

Activate env:
windows:
env\Scripts\Activate.ps1 

mac:
source env/bin/activate


Deactive:
deactivate

Install requirements:
pip install -r requirements.txt

Generate requirements:
pip freeze > requirements.txt

###################

- live sass extension, and use watch sass to create css

- create home page, and home page route on flask:
@app.route("/")
def index():
    return render_template("index.html")

- main method
if __name__ == "__main__":
    app.run(debug=True)


-- 

Day 2: 13 Feb 2025

- Created routes for index, update and delete, routes have to match FE, grab content dynamically, FE display content dynamically 

- Initial deployment on pythonanywhere, using BASH, venv and WSGI config file:
wsgi config:

import sys
path = '/home/laiweijie88/full_stack_w_ai'
if path not in sys.path:
    sys.path.append(path)
from app import app as application


- task = Todo.query.get_or_404(id)
eliminates the need to manually check for if task is  None, as it throws an error 


- python type hinting: specifies expected input and return
def get_task(id: int) -> str:
    return f"Task {id}"

- navigating sql from terminal:

    cd to database.db
    sqlite3 database.db #open shell

    .tables             #list tables
    select * from table #show rows

- *** SQLite only creates db once, if schema changes, have to manually alter tables, or drop and recreate db

- return render_template('index.html', tasks=tasks)

LHS (tasks): This is the variable name that will be available inside index.html.
RHS (tasks): This is the Python variable from app.py (which contains the list of Todo objects).

- adding additional due date column in the page:

1. add due date table header, and task.due_date (+exception handling)
2. add due date to db schema
3. add due date to index, (get due date from input, save as new_task and passed to db)


-------

Day 3 : 19 Feb 2025

-✅ Use request.form['key'] if the field is required and must exist (but use try-except to catch errors).
✅ Use request.form.get('key') for optional fields or when avoiding crashes is important.

username = request.form.get('username')
Returns None if the field is missing, preventing crashes.
Allows setting a default value:
username = request.form.get('username', 'Guest')



- @app.route("/register", methods=["POST"])
This route is triggered only when the form is submitted (POST method).
If a user tries to visit /register directly via browser (GET method), they'll get an error.

-regex for strong passwords:
import re

def is_strong_password(password):
    return (
        len(password) >= 8 and  # At least 8 characters
        any(char.isdigit() for char in password) and  # At least 1 number
        any(char.isupper() for char in password) and  # At least 1 uppercase letter
        any(char.islower() for char in password)  # At least 1 lowercase letter
    )







---- 









