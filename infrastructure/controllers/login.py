from _curses import flash
from functools import wraps

import bcrypt as bcrypt
from flask import current_app as app, redirect, request, render_template, url_for, session
from flask_login import login_required, logout_user, login_user

from infrastructure.repository.models.user import UserModel
from infrastructure.repository.user import UserRepository


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect((url_for('login')))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = UserRepository().get_user_with_credentials(request.form['username'],
                                                          request.form['password'])
        if not user:
            error = 'Invalid Credentials. Please try again.'
            return render_template('login.html', error=error), 401
        login_user(user)
        return redirect(url_for('get_all_units'))
    return render_template('login.html', error=error)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        user = UserModel()
        user.username = request.form['username']
        user.password = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
        UserRepository().save(user)
        login_user(user)
        return redirect(url_for('get_all_units'))
    return render_template('signup.html', error=error)


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('/login'))

    return wrap
