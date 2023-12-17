from main.models import User, Trip, Schedule
from main import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request
from main.forms import RegistrationForm, LoginForm, SearchForm
from flask_login import login_user, current_user, logout_user, login_required
from datetime import date


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')




@app.route("/schedule")
def schedule():
    return render_template("schedule.html", title="Schedule")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, phone=form.phone.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Ваш аккаунт було створено! У вас є можливість увійти в систему", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)


@app.route("/login", methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Помилка входу. Перевірте номер телефону, email або пароль', 'danger')
    return render_template('login.html', title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title="Account")

