from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    # Return this as a strange
    return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application-form")
def application_page():
	return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def application(): 
	first_name = request.form.get("firstname")
	last_name = request.form.get("lastname")
	salary = request.form.get("salary")
	job = request.form.get("job")
	return render_template("application.html", jinja_first=first_name, jinja_last=last_name, jinja_salary=salary, jinja_job=job)

if __name__ == "__main__":
    app.run(debug=True)