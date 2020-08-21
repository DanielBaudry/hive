from flask import current_app as app, render_template, request

from infrastructure.controllers.serializer.planet_serializer import serialize_planets
from infrastructure.dependencies_injections import list_planets_in_solar_system


@app.route('/univers', methods=['GET'])
def get_univers_map():
    solar_system = int(request.args.get('solar_system', '1'))
    planets = list_planets_in_solar_system.execute(solar_system=solar_system)
    serialized_planets = serialize_planets(planets=planets)
    return render_template('univers.html', planets=serialized_planets), 200
