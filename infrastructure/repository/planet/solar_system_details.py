from enum import Enum

from infrastructure.repository.unit.units_details import UnitsInMemory


class SolarSystemsInMemory(Enum):
    S1 = {
        'id': 1,
        'planets': [
            {
                'id': 1,
                'position': 1,
                'planet_forces': [
                    {
                        'unit_name': 'MARINE',
                        'quantity': 1200,
                        'outpost_id': 1,
                    },
                    {
                        'unit_name': 'TANK',
                        'quantity': 210,
                        'outpost_id': 1,
                    },
                    {
                        'unit_name': 'MARINE',
                        'quantity': 1200,
                        'outpost_id': 2,
                    },
                ],
            },
            {
                'id': 2,
                'position': 2,
            },
            {
                'id': 3,
                'position': 3,
            }
        ]
    }

    S2 = {
        'id': 2,
        'planets': [
            {
                'id': 11,
                'position': 1,
            },
            {
                'id': 12,
                'position': 2,
            },
            {
                'id': 13,
                'position': 3,
            }
        ]
    }
