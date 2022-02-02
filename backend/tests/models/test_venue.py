from api.models.venue import Venue
from api.lib.orm import save
from api.lib.db import drop_records, drop_tables, test_conn, test_cursor
import pytest

def test_initialize_with_values_of_foursquare_id_name_rating_likes():
    venue = Venue(foursquare_id = '5b2932a0f5e9d70039787cf2',
            name = 'Los Tacos', rating = 5, likes = 20, menu_url = 'foobar.com')
    assert venue.__dict__ == {'foursquare_id': '5b2932a0f5e9d70039787cf2',
        'name': 'Los Tacos', 'likes': 20, 'menu_url': 'foobar.com', 'rating': 5}

@pytest.fixture()
def clean_tables():
    drop_records(test_cursor, test_conn, 'venues')
    yield
    drop_records(test_cursor, test_conn, 'venues')

def test_saves_to_the_db(clean_tables):
        venue = Venue(foursquare_id = '1245', name = 'Los Tacos',
        price = 2, rating = 3.5, likes = 100, menu_url = 'www.foobar.com'
        )
        save(venue, test_conn, test_cursor)
        test_cursor.execute('SELECT * FROM venues ORDER BY id DESC LIMIT 1')
        record = test_cursor.fetchone()
        assert record[1:3] == ('1245', 'Los Tacos')