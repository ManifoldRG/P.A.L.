from enum import Enum
from datetime import datetime, time
import json
from ..proactive_plugin import ProactivePlugin

"""
TODO:
- integrate timer to iterate through nearby places
- refactor such that location API could be used and track location data
  and pull nearby places
- potentially allow for user interest to be passed in
"""

class PlacesCategory(Enum):
    RESTAURANT = 'RESTAURANT'
    FAST_FOOD = 'FAST_FOOD'
    BAR = 'BAR'
    EVENT = 'EVENT'
    CAFE = 'CAFE'
    THEATER = 'THEATER'
    MEDICAL = 'MEDICAL'
    LIBRARY = 'LIBRARY'
    BOOKSTORE = 'BOOKSTORE'


class NearbyPlacesPlugin(ProactivePlugin):
    def __init__(self):
        self.nearby_places_list = NEARBY_PLACES_LIST
        self.start_time = datetime.now().time()


    def get_nearby_places(self):
        if self.nearby_places_list:
            return str(json.dumps(self.nearby_places_list.pop(0), indent=2))
        return None


NEARBY_PLACES_LIST = [
    [
        {
            "name": "Keddy's Cafe",
            "address": "51 Astor Pl, New York, NY 10003",
            "category": str(PlacesCategory.CAFE.value),
            "open_now": True,
        },
        {
            "name": "Mamoun's Falafel",
            "address": "30 St Marks Pl, New York, NY 10003",
            "category": PlacesCategory.RESTAURANT.value,
            "open_now": True,
        },
        {
            "name": "Cooper Union Libary",
            "address": "55 E 8th St, New York, NY 10003",
            "category": PlacesCategory.LIBRARY.value,
            "open_now": True,
        },
        {
            "name": "Grey Art Museum",
            "address": "95 Astor Pl, New York, NY 10003",
            "category": PlacesCategory.FAST_FOOD.value,
            "open_now": True,
        },
        {
            "name": "Brooklyn Bagel Company",
            "address": "41 E 6th St, New York, NY 10003",
            "category": PlacesCategory.FAST_FOOD.value,
            "open_now": True,
        },
    ],
    [
        {
            "name": "Strand Bookstore",
            "address": "51 Astor Pl, New York, NY 10003",
            "category": PlacesCategory.BOOKSTORE.value,
            "open_now": True,
        },
        {
            "name": "New York Public Library",
            "address": "30 St Marks Pl, New York, NY 10003",
            "category": PlacesCategory.RESTAURANT.value,
            "open_now": True,
        },
        {
            "name": "Chipotle",
            "address": "55 E 8th St, New York, NY 10003",
            "category": PlacesCategory.FAST_FOOD.value,
            "open_now": True,
        },
        {
            "name": "The Long Pour",
            "address": "92 E 7th St, New York, NY 10003",
            "category": PlacesCategory.BAR.value,
            "open_now": True,
        },
        {
            "name": "Amsterdam Pool Hall",
            "address": "41 Broadway, New York, NY 10003",
            "category": PlacesCategory.BAR.value,
            "open_now": True,
        },
    ],
    [
        {
            "name": "Starbucks",
            "address": "51 Astor Pl, New York, NY 10003",
            "category": PlacesCategory.CAFE.value,
            "open_now": True,
        },
        {
            "name": "Dunkin Donuts",
            "address": "30 St Marks Pl, New York, NY 10003",
            "category": PlacesCategory.CAFE.value,
            "open_now": True,
        },
        {
            "name": "The Ivory Peacock",
            "address": "55 E 8th St, New York, NY 10003",
            "category": PlacesCategory.BAR.value,
            "open_now": True,
        },
        {
            "name": "AMC Theatres",
            "address": "92 E 7th St, New York, NY 10003",
            "category": PlacesCategory.THEATER.value,
            "open_now": True,
        },
        {
            "name": "The PIT",
            "address": "41 Broadway, New York, NY 10003",
            "category": PlacesCategory.EVENT.value,
            "open_now": True,
        },
    ],
    [
        {
            "name": "787 Coffee",
            "address": "51 Astor Pl, New York, NY 10003",
            "category": PlacesCategory.CAFE.value,
            "open_now": True,
        },
        {
            "name": "New York Public Library",
            "address": "30 St Marks Pl, New York, NY 10003",
            "category": PlacesCategory.RESTAURANT.value,
            "open_now": True,
        },
        {
            "name": "Chipotle",
            "address": "55 E 8th St, New York, NY 10003",
            "category": PlacesCategory.FAST_FOOD.value,
            "open_now": True,
        },
        {
            "name": "The Long Pour",
            "address": "92 E 7th St, New York, NY 10003",
            "category": PlacesCategory.BAR.value,
            "open_now": True,
        },
        {
            "name": "Amsterdam Pool Hall",
            "address": "41 Broadway, New York, NY 10003",
            "category": PlacesCategory.BAR.value,
            "open_now": True,
        },
    ]
]
