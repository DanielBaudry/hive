from flask import current_app as app, render_template
from flask_login import current_user

from infrastructure.controllers.serializer.hive_unit_serializer import serialize_resources, serialize_hive_units
from infrastructure.dependencies_injections import get_user_resources, list_all_hive_units, list_all_units


@app.route('/battlemap', methods=['GET'])
def get_war_panel():
    units = list_all_units.execute()
    hive_units = list_all_hive_units.execute(user_id=current_user.id)
    resources = get_user_resources.execute(user_id=current_user.id)
    serialzed_hive_units = serialize_hive_units(hive_units, units)
    serialzed_resources = serialize_resources(resources)
    return render_template('battlemap.html', units=serialzed_hive_units, resources=serialzed_resources), 200
