from flask import current_app as app
from flask_login import login_required, current_user

from infrastructure.dependencies_injections import provide_get_all_hive_units_use_case


@app.route('/units', methods=['GET'])
@login_required
def get_all_units():
    units = provide_get_all_hive_units_use_case().get_all_hive_units(current_user.id)
    return str(units), 200


@app.route('/units', methods=['POST'])
def create_new_units():
    return '', 200
