from api.models.venue import Venue
class VenueBuilder:
    def __init__(self, response_venue):
        self.response_venue = response_venue

    def select_attributes(self):
        foursquare_id = self.response_venue['id']
        venue_name = self.response_venue['name']
        price = self.response_venue['price']['tier']
        likes = self.response_venue['likes']['count']
        menu_url = self.response_venue.get('delivery', '')
        if menu_url:
            menu_url = menu_url.get('url', '').split('?')[0]
        vals = [foursquare_id, venue_name, price, likes, menu_url]
        keys = ['foursquare_id', 'name', 'price', 'likes', 'menu_url']
        attr = dict(zip(keys, vals))
        return attr

    def run(self):
        attr = self.select_attributes()
        venue = Venue(**attr)
        return venue