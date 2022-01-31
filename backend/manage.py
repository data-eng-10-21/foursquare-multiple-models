from api.models.venue import Venue
from api.adapters.client import Client
from api.adapters.venue_builder import VenueBuilder

def run():
    client = Client()
    venues_from_api = client.request_venues()
    builder = VenueBuilder(venues_from_api)
    venues = builder.run()
    return venues

