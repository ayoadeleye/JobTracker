from flask import Flask, render_template, redirect, url_for, flash, request
from jobTracker import app, db, bcrypt
from flask_login import current_user
from jobTracker.signin import SignInForm
from jobTracker.models import User


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route("/signin", methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')

    return render_template("signin.html")


