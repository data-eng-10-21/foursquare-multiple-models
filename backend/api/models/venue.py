class Venue:
    columns = ['foursquare_id', 'name', 'price',
            'rating', 'likes', 'menu_url']
    __table__ = 'venues'
    
    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}' 
        for k, v in kwargs.items():
            setattr(self, k, v)