from models.venue import Venue
from adapters.client import Client
from adapters.venue_builder import VenueBuilder

def run():
    client = Client()
    venues_from_api = client.request_venues()
    builder = VenueBuilder(venues_from_api)
    venues = builder.run()
    return venues

