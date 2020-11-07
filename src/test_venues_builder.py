from venues_builder import VenuesBuilder
from venue import Venue

venues_from_api = [{'id': '5b2932a0f5e9d70039787cf2', 'name': 'Los Tacos Al Pastor', 'location': {'address': '141 Front St', 'lat': 40.70243624175102, 'lng': -73.98753900608666, 'labeledLatLngs': [{'label': 'display', 'lat': 40.70243624175102, 'lng': -73.98753900608666}], 'distance': 1086, 'postalCode': '11201', 'cc': 'US', 'neighborhood': 'DUMBO', 'city': 'New York', 'state': 'NY', 'country': 'United States', 'formattedAddress': ['141 Front St', 'New York, NY 11201', 'United States']}, 'categories': [{'id': '4bf58dd8d48988d151941735', 'name': 'Taco Place', 'pluralName': 'Taco Places', 'shortName': 'Tacos', 'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/taco_', 'suffix': '.png'}, 'primary': True}], 'delivery': {'id': '857049', 'url': 'https://www.seamless.com/menu/los-tacos-al-pastor-141a-front-st-brooklyn/857049?affiliate=1131&utm_source=foursquare-affiliate-network&utm_medium=affiliate&utm_campaign=1131&utm_content=857049', 'provider': {'name': 'seamless', 'icon': {'prefix': 'https://fastly.4sqi.net/img/general/cap/', 'sizes': [40, 50], 'name': '/delivery_provider_seamless_20180129.png'}}}, 'referralId': 'v-1604712009', 'hasPerk': False}, {'id': '542f62bc498ee31baa1395cb', 'name': "Rocco's Tacos and Tequila Bar Brooklyn", 'location': {'address': '339 Adams St', 'lat': 40.693277341475834, 'lng': -73.98868115958473, 'labeledLatLngs': [{'label': 'display', 'lat': 40.693277341475834, 'lng': -73.98868115958473}, {'label': 'entrance', 'lat': 40.692728, 'lng': -73.988616}], 'distance': 1213, 'postalCode': '11201', 'cc': 'US', 'city': 'Brooklyn', 'state': 'NY', 'country': 'United States', 'formattedAddress': ['339 Adams St', 'Brooklyn, NY 11201', 'United States']}, 'categories': [{'id': '4bf58dd8d48988d1c1941735', 'name': 'Mexican Restaurant', 'pluralName': 'Mexican Restaurants', 'shortName': 'Mexican', 'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/mexican_', 'suffix': '.png'}, 'primary': True}], 'referralId': 'v-1604712009', 'hasPerk': False}]


# Above we are taking some sample data from the api, and now will need to create
# a VenuesBuilder that can take that messy data, extract the relevant data from 
# each dictionary, and use that data to initialize separate Venue instances.

# We break this into steps.

# 1. First, we should define VenuesBuilder so that 
# it is initialized with the list of venue dictionaries from our api

def test_initializes_with_list_of_venues():
    builder = VenuesBuilder(venues_from_api)
    assert isinstance(builder.venues_from_api, list) == True

def test_does_not_change_inputted_venues_when_storing_on_the_instance():
    builder = VenuesBuilder(venues_from_api)
    assert builder.venues_from_api[0] == venues_from_api[0]

# Then we define a run function.  This function starts with the `venues_from_api# ` list of dictionaries and returns a Venue instance initialized with the appro# priate data.  

def test_builds_an_instance_for_each_venue():
    builder = VenuesBuilder(venues_from_api)
    venues = builder.run()
    assert len(venues) == len(venues_from_api)

def test_each_instance_is_venue():
    builder = VenuesBuilder(venues_from_api)
    venues = builder.run()
    first_venue = venues[0]
    assert isinstance(first_venue, Venue)

def test_extracts_id_name_lat_long_category_zip_and_initialize_venue():
    builder = VenuesBuilder(venues_from_api)
    venues = builder.run()
    first_venue = venues[0]
    list(first_venue.__dict__.keys()) == ['id', 'name', 'latitude', 'longitude', 'category', 'zip_code']

    assert list(first_venue.__dict__.values()) == ['5b2932a0f5e9d70039787cf2', 'Los Tacos Al Pastor', -73.98753900608666, 40.70243624175102, '11201', 'Tacos']
