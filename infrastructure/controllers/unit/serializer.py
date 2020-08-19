from typing import Dict, List

from domain.unit.unit import Unit


def _serialize_unit(unit: Unit) -> Dict:
    return {
        'name': unit.name,
    }


def serialize_units(units: List[Unit]):
    return [_serialize_unit(unit) for unit in units]
