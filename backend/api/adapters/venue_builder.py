from api.models.venue import Venue
class VenueBuilder:
    def __init__(self, venues_from_api):
        self.venues_from_api = venues_from_api

    def run(self):
        venues = []
        for venue_from_api in self.venues_from_api:
            venue_id = venue_from_api['id']
            venue_name = venue_from_api['name']
            lat = venue_from_api['location']['lat']
            long = venue_from_api['location']['lng']
            category = venue_from_api['categories'][0]['shortName']
            zip_code = venue_from_api['location'].get('postalCode')
            venue = Venue(id = venue_id, name = venue_name, 
                    latitude = lat, longitude = long, 
                    category = category, zip_code = zip_code)
            venues.append(venue)
        return venues
