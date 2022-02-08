from api.models import Category, VenueCategory
from api.lib.orm import save, find_or_create_by_name
class CategoryBuilder:
    def __init__(self, response_venue = {}):
        self.response_venue = response_venue

    def select_attributes(self):
        categories = [category['name'] for category in self.response_venue['categories']]
        return categories

    def find_or_create_categories(self, category_names, conn, cursor):
        if not isinstance(category_names, list): raise TypeError('category_names must be list')
        categories = []
        for name in category_names:
            category = find_or_create_by_name(Category, 
                name, conn, cursor)
            categories.append(category)
        return categories
    
    def create_venue_categories(self, venue, categories, conn, cursor):
        categories = [VenueCategory(venue_id = venue.id, category_id = category.id)
                for category in categories]
        return [save(category, conn, cursor) for category in categories]


    def run(self, venue_details, venue, conn, cursor):
        category_names = self.select_attributes()
        categories = self.find_or_create_categories(category_names, conn, cursor)
        venue_categories = self.create_venue_categories(venue, categories, conn, cursor)
        return venue_categories