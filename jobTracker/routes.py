from flask import Flask, render_template


app = Flask(__name__)
app.secret_key = 'secret string'


jobs = [
    {
        'job_title': 'Software Engineer Intern',
        'company': 'Meta',
        'location': 'First Post',
        'date_applied': 'Feb 17, 2022',
        'status': 'Applied',
        'notes': 'housing benefits'
    },
    {
        'job_title': 'Software Engineer Intern',
        'company': 'Meta',
        'location': 'First Post',
        'date_applied': 'Feb 17, 2022',
        'status': 'Applied',
        'notes': 'housing benefits'
    }
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signin")
def signin():
    return render_template("signin.html")


