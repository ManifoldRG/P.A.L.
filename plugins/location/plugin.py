from enum import Enum
from datetime import datetime, time
import json
import random
from utils import get_client
from ..proactive_plugin import ProactivePlugin

"""
- integrate timer to iterate through nearby places
- refactor such that location API could be used and track location data
  and pull nearby places
- potentially allow for user interest to be passed in
"""

class PlacesCategory(Enum):
    BAR = 'BAR'
    BOOKSTORE = 'BOOKSTORE'
    CAFE = 'CAFE'
    COWORKING = 'COWORKING'
    EVENT = 'EVENT'
    FAST_FOOD = 'FAST_FOOD'
    MEDICAL = 'MEDICAL'
    LANDMARK = 'LANDMARK'
    LIBRARY = 'LIBRARY'
    RESTAURANT = 'RESTAURANT'
    THEATER = 'THEATER'


class LocationPlugin(ProactivePlugin):
    def __init__(self):
        self.nearby_places_list = NEARBY_PLACES_LIST
        self.start_time = datetime.now().time()
        self.triggered = False
        self.client = get_client()


    def invoke(self, event):
        if self.nearby_places_list:
            transcripts = "Nearby locations: "
            transcripts += str(json.dumps(self.nearby_places_list.pop(0), indent=2))
            return transcripts


NEARBY_PLACES_LIST = [
    [
        {
            "name": "Golden Goat Coffee",
            "address": "599 3rd St #100, San Francisco, CA 94107",
            "category": PlacesCategory.CAFE.value,
            "open_now": True,
        },
        {
            "name": "Rooh SF",
            "address": "333 Brannan St #150, San Francisco, CA 94107",
            "category": PlacesCategory.RESTAURANT.value,
            "open_now": True,
        },
        {
            "name": "CrossFit South Park",
            "address": "361 Brannan St, San Francisco, CA 94107",
            "category": PlacesCategory.LIBRARY.value,
            "open_now": True,
        },
        {
            "name": "Founders Den",
            "address": "665 3rd St #150, San Francisco, CA 94107",
            "category": PlacesCategory.COWORKING.value,
            "open_now": True,
        },
        {
            "name": "South Park",
            "address": "64 S Park St, San Francisco, CA 94107",
            "category": PlacesCategory.FAST_FOOD.value,
            "open_now": True,
        },
    ],
    [
        {
            "name": "Oracle Park",
            "address": "24 Willie Mays Plaza, San Francisco, CA 94107",
            "category": PlacesCategory.BOOKSTORE.value,
            "open_now": True,
        },
        {
            "name": "Lucky Strike",
            "address": "24 Willie Mays Plaza, San Francisco, CA 94107",
            "category": PlacesCategory.RESTAURANT.value,
            "open_now": True,
        },
        {
            "name": "Orangetheory Fitness",
            "address": "215 King St, San Francisco, CA 94107",
            "category": PlacesCategory.FAST_FOOD.value,
            "open_now": True,
        },
        {
            "name": "ChargePoint Charging Station",
            "address": "250 King St, San Francisco, CA 94107",
            "category": PlacesCategory.BAR.value,
            "open_now": True,
        },
        {
            "name": "Saison",
            "address": "178 Townsend St, San Francisco, CA 94107",
            "category": PlacesCategory.BAR.value,
            "open_now": True,
        },
    ],
    [
        {
            "name": "Oracle Park",
            "address": "24 Willie Mays Plaza, San Francisco, CA 94107",
            "category": PlacesCategory.BOOKSTORE.value,
            "open_now": True,
        },
        {
            "name": "Lucky Strike",
            "address": "24 Willie Mays Plaza, San Francisco, CA 94107",
            "category": PlacesCategory.RESTAURANT.value,
            "open_now": True,
        },
        {
            "name": "Orangetheory Fitness",
            "address": "215 King St, San Francisco, CA 94107",
            "category": PlacesCategory.FAST_FOOD.value,
            "open_now": True,
        },
        {
            "name": "ChargePoint Charging Station",
            "address": "250 King St, San Francisco, CA 94107",
            "category": PlacesCategory.BAR.value,
            "open_now": True,
        },
        {
            "name": "Saison",
            "address": "178 Townsend St, San Francisco, CA 94107",
            "category": PlacesCategory.BAR.value,
            "open_now": True,
        },
    ],
    [
        {
            "name": "Oracle Park",
            "address": "24 Willie Mays Plaza, San Francisco, CA 94107",
            "category": PlacesCategory.BOOKSTORE.value,
            "open_now": True,
        },
        {
            "name": "Lucky Strike",
            "address": "24 Willie Mays Plaza, San Francisco, CA 94107",
            "category": PlacesCategory.RESTAURANT.value,
            "open_now": True,
        },
        {
            "name": "Orangetheory Fitness",
            "address": "215 King St, San Francisco, CA 94107",
            "category": PlacesCategory.FAST_FOOD.value,
            "open_now": True,
        },
        {
            "name": "ChargePoint Charging Station",
            "address": "250 King St, San Francisco, CA 94107",
            "category": PlacesCategory.BAR.value,
            "open_now": True,
        },
        {
            "name": "Saison",
            "address": "178 Townsend St, San Francisco, CA 94107",
            "category": PlacesCategory.BAR.value,
            "open_now": True,
        },
    ],
]
