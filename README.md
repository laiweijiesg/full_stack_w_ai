# full_stack_w_ai
Feb Project: Full Stack App w ML Component: Stock market (time series) or HDB Prices 

start : 11 Feb 2025 

---

Day 1: 11 Feb 2025

Create venv:
python3 -m venv env

Activate env:
env\Scripts\Activate.ps1 

Deactive:
deactivate

Generate requirements:
pip freeze > requirements.txt

###################

live sass extension, and use watch sass to create css

create home page, and home page route on flask:
@app.route("/")
def index():
    return render_template("index.html")

if __name__ in "__main__":
    app.run(debug=True)








