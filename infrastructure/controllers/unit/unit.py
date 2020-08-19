from flask import current_app as app, render_template

from infrastructure.controllers.unit.serializer import serialize_units
from infrastructure.dependencies_injections import list_all_units


@app.route('/units', methods=['GET'])
def list_units():
    units = list_all_units.execute()
    serialized_units = serialize_units(units)
    return render_template('unit.html', units=serialized_units), 201
