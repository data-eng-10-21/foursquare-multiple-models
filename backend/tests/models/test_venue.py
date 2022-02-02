from api.models.venue import Venue

def test_initialize_with_values_of_foursquare_id_name_rating_likes_menu_url():
    venue = Venue(foursquare_id = '5b2932a0f5e9d70039787cf2',
            name = 'Los Tacos', rating = 5, likes = 20, menu_url = 'foobar.com')
    assert venue.__dict__ == {'foursquare_id': '5b2932a0f5e9d70039787cf2',
    'name': 'Los Tacos', 'likes': 20, 'menu_url': 'foobar.com', 'rating': 5}