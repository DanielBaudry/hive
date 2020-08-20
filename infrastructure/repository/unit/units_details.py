from enum import Enum


class UnitsInMemory(Enum):
    ZERGLING = {
        'display_name': 'Zergling',
        'cost': 10,
        'life': 40,
        'damage': 5,
    }

    ROACH = {
        'display_name': 'Roach',
        'cost': 50,
        'life': 220,
        'damage': 20,
    }

    HYDRALISK = {
        'display_name': 'Hydralisk',
        'cost': 70,
        'life': 160,
        'damage': 40,
    }

    ULTRALISK = {
        'display_name': 'Ultralisk',
        'cost': 100,
        'life': 500,
        'damage': 50,
    }
