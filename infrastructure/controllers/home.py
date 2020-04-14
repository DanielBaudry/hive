from flask import current_app as app, render_template


@app.route('/home')
def home():
    return 'Hello World!'


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')
