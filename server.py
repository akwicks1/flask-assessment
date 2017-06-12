from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

JOBS = ["software engineer", "QA engineer", "product manager"]
# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route('/')
def index():
	"""Show the home page."""
	return render_template("index.html")

@app.route('/application-form')
def application():
	"""Show application form."""

	return render_template("application-form.html",
							jobs=JOBS)

@app.route('/application-success', methods=['POST'])
def successful_application():
	"""Show successful application."""

	firstname = request.form.get("firstname")
	lastname = request.form.get("lastname")
	jobtitle = request.form.get("jobtitle")
	salary = request.form.get("salary")

	return render_template("application-response.html",
							firstname=firstname,
							lastname=lastname,
							jobtitle=jobtitle,
							salary=salary)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
