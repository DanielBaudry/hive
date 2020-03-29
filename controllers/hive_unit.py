from flask import current_app as app
from flask_login import login_required, current_user

from use_cases.get_all_hive_units import get_all_hive_units


@app.route('/units', methods=['GET'])
@login_required
def get_all_units():
    units = get_all_hive_units(current_user.id)
    return str(units), 200


@app.route('/units', methods=['POST'])
def create_new_units():
    return '', 200
