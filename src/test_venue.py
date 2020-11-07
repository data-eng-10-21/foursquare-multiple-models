from venue import Venue

# Here we test that our venue class is set up properly.  
# We should have the ability to initialize a Venue instance with the 
# attributes below, and it should set the attributes of the instance accordingly.

def test_initialize_with_values_of_id_name_latitude_longitude_category_zip_code():
    venue = Venue(id = '1234', 
            name = 'Los Tacos', longitude = -73.98, 
            latitude = 40.7, zip_code = '11201', category = 'Tacos')
    assert venue.__dict__ == {'id': '1234', 'name': 'Los Tacos',
  'longitude': -73.98, 'latitude': 40.7, 'zip_code': '11201',
  'category': 'Tacos'}
