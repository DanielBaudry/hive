from flask import current_app as app
from flask_login import login_required


@app.route('/planets', methods=['GET'])
@login_required
def get_all_planets():
    return 'Planets', 200
