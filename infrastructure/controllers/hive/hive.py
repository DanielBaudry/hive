from flask import current_app as app, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from infrastructure.controllers.serializer.hive_unit_serializer import serialize_hive_units, serialize_resources
from infrastructure.dependencies_injections import list_all_hive_units, spawn_new_hive_units, list_all_units, \
    get_user_resources


@app.route('/hive', methods=['GET'])
@login_required
def get_hive():
    units = list_all_units.execute()
    hive_units = list_all_hive_units.execute(user_id=current_user.id)
    resources = get_user_resources.execute(user_id=current_user.id)
    serialzed_hive_units = serialize_hive_units(hive_units, units)
    serialzed_resources = serialize_resources(resources)
    return render_template('hive.html', units=serialzed_hive_units, resources=serialzed_resources), 200


@app.route('/hiveunit', methods=['POST'])
@login_required
def create_hive_unit():
    unit_name = request.form['unit_name']
    quantity = int(request.form['quantity'])
    spawn_new_hive_units.execute(user_id=current_user.id, unit_name=unit_name, quantity=quantity)
    return redirect(url_for('get_hive'))
