import pyablo

class Account(pyablo._FetchMixin):

    _PATH = 'account/'
    
    def __init__(self, api, name, region=None, locale=None, json=None):
        if not region: region = api.region
        if not locale: locale = api.locale
        self._api = api
        self._name = name
        self._region = region
        self._locale = locale
        self._json = json
        
        # Split battletag for the url
        self._bt_name, self._bt_id = self._name.split('#')
        
        self._url = pyablo.REGION[region]['prefix'] + self._PATH + \
                    self._bt_name + '-' + self._bt_id
                    
    @property
    def name(self):
        """Return the account name in the form Name#1234"""
        return self._name
        
    @property
    def heroes(self):
        """
        Return a list of `pyablo.Hero` objects representing the heroes the
        account owns.
        
        """
        data = self._json_property('heroes')
        ret = []
        for id in data:
            ret.append(self.get_hero(id, region=self._region,
                                   locale=self._locale))
        return ret
        
    @property
    def last_hero_played(self):
        """
        Return a `pyablo.Hero` object representing the last hero played by
        the account.
        
        
        """
        id = self._json_property('last-hero-played')
        return self.get_hero(id)
        
    @property
    def artisans(self):
        """
        Return a list of dictionaries defining the account's artisans.
        
        """
        data = self._json_property('artisans')
        ret = []
        for artisan in data:
            pyart = {
                'slug' : artisan['slug'],
                'level' : artisan['level'],
                'step_current' : artisan['step-current'],
                'step_max' : artisan['step-max'],
            }
            ret.append(pyart)
        return ret
        
    @property
    def hardcore_artisans(self):
        """
        Return a list of dictionaries defining the account's artisans on
        hardcore mode.
        
        """
        data = self._json_property('hardcore-artisans')
        ret = []
        for artisan in data:
            pyart = {
                'slug' : artisan['slug'],
                'level' : artisan['level'],
                'step_current' : artisan['step-current'],
                'step_max' : artisan['step-max'],
            }
            ret.append(pyart)
        return ret
        
    @property
    def progression(self):
        """
        Return a list of dictionaries defining the account's progression.
        
        """
        return self._json_property('progression')
        
    @property
    def kills(self):
        """
        Returns a dictionary defining the account's total kills.
        
        """
        data = self._json_property('kills')
        
        ret = {
            'monsters' : data['monsters'],
            'elites' : data['elites'],
            'hardcore_monsters' : data['hardcoreMonsters']
        }
        
        return ret
        
    @property
    def time_played(self):
        """
        Returns a dictionary defining the time played for each class as a
        ratio.
        
        """
        return self._json_property('time-played')
        
    def get_hero(self, id, region=None, locale=None, json=None):
        """
        Return the hero `id` from this account.
        
        """
        return self._api.get_hero(self, id, region=region, locale=locale,
                                  json=json)