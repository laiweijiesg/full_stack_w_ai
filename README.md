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









