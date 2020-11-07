from venue import Venue
from client import Client
from venues_builder import VenuesBuilder

def run():
    client = Client()
    venues_from_api = client.request_venues()
    builder = VenuesBuilder(venues_from_api)
    venues = builder.run()
    return venues

