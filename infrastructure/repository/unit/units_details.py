from enum import Enum


class UnitsInMemory(Enum):
    ZERGLING = {
        'display_name': 'Zergling',
        'cost': 10,
        'life': 40,
        'damage': 5,
        'planet_force_only': False,
    }

    ROACH = {
        'display_name': 'Roach',
        'cost': 50,
        'life': 220,
        'damage': 20,
        'planet_force_only': False,
    }

    HYDRALISK = {
        'display_name': 'Hydralisk',
        'cost': 70,
        'life': 160,
        'damage': 40,
        'planet_force_only': False,
    }

    ULTRALISK = {
        'display_name': 'Ultralisk',
        'cost': 100,
        'life': 500,
        'damage': 50,
        'planet_force_only': False,
    }

    MARINE = {
        'display_name': 'Marine',
        'cost': 50,
        'life': 50,
        'damage': 10,
        'planet_force_only': True,
    }

    TANK = {
        'display_name': 'Tank',
        'cost': 120,
        'life': 200,
        'damage': 50,
        'planet_force_only': True,
    }
