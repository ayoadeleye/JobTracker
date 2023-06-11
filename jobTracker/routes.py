from flask import render_template, redirect, url_for, flash, request
from jobTracker import app, db, bcrypt
from flask_login import current_user, login_user, logout_user, login_manager
from jobTracker.forms import RegistrationForm, LoginForm
from jobTracker.models import User
from scraper import scrape_indeed_jobs 


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for!', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title='Registration', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash('Login Successful.', 'success')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template("login.html", title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    jobs = scrape_indeed_jobs(query)
    return render_template('results.html', jobs=jobs)
