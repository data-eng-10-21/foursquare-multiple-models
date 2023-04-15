from api.adapters.client import Client

def test_client_created_with_client_id():
    client = Client()
    assert isinstance(client.CLIENT_ID, str) == True, 'CLIENT_ID is not a string'

def test_client_created_with_client_secret():
    client = Client()
    assert isinstance(client.CLIENT_SECRET, str) == True, 'CLIENT_SECRET is not a string'

def test_client_created_with_date():
    client = Client()
    assert isinstance(client.DATE, str) == True, 'DATE is not a string'

def test_client_created_with_url():
    client = Client()
    assert client.URL == "https://api.foursquare.com/v2/venues/search"

def test_auth_params_returns_dictionary_of_client_id_secret_and_v():
    client = Client()
    assert list(client.auth_params().keys()) == ['client_id', 'client_secret', 'v']

def test_full_params_returns_dictionary_of_auth_params_combined_with_additional_query_params():
    client = Client()
    assert list(client.full_params(query_params = {'ll': '40.7,-74', 'query': 'tacos'}).keys()) == ['client_id', 'client_secret', 'v', 'll', 'query']

def test_request_venues_makes_request_to_foursquare_api_with_url_and_full_params():
    client = Client()
    first_venue_returned = client.request_venues()[0]
    sorted_keys = list(sorted(first_venue_returned.keys()))
    assert  sorted_keys == ['categories', 'createdAt', 'delivery',
                             'hasPerk', 'id', 'location', 'name', 'referralId']

def test_request_venue():
    client = Client()
    venue_id = '5b2932a0f5e9d70039787cf2'
    venue_details = client.request_venue(venue_id)
    venue_keys = sorted(list(venue_details.keys()))
    
    venue_keys == ['allowMenuUrlEdit', 'attributes', 'beenHere', 'bestPhoto',
                    'canonicalUrl', 'categories', 'contact', 'createdAt',
                      'defaultHours', 'delivery', 'dislike', 'hereNow',
                        'hours', 'id', 'inbox', 'likes', 'listed',
                          'location', 'name', 'ok', 'pageUpdates',
                            'photos', 'phrases', 'popular', 'price',
                              'rating', 'ratingColor', 'ratingSignals', 'reasons',
                                'seasonalHours', 'shortUrl', 'stats', 'timeZone',
                                  'tips', 'url', 'verified']