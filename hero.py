import pyablo

class Hero(pyablo._FetchMixin):
    """
    Encapsulates a Diablo 3 hero.
    
    """
    
    _PATH = 'account/'
    _PATH2 = '/hero/'
    
    def __init__(self, api, account, id, region=None, locale=None, json=None):
        """
        
        """
        if not region: region = api.region
        if not locale: locale = api.locale
        if isinstance(account, pyablo.Account):
            # Get the account name if an Account object is passed
            account = account.name
        self._api = api
        self._id = id
        self._region = region
        self._locale = locale
        self._json = json
        self._bt = account.replace('#', '-')
        
        self._url = pyablo.REGION[region]['prefix'] + self._PATH + self._bt \
                    + self._PATH2 + str(id)
        
    @property
    def id(self):
        """
        Return the hero's id.
        
        """
        return self._id
        
    @property
    def name(self):
        """
        Return the hero's name.
        
        """
        return self._json_property('name')
        
    @property
    def hardcore(self):
        """Return True if the hero is a hardcore hero."""
        return self._json_property('hardcore')
        
    @property
    def hero_class(self):
        """
        Returns the hero's class.
        
        """
        return self._json_property('class')
        
    @property
    def level(self):
        """Return the hero's level."""
        return self._json_property('level')
        
    @property
    def gender(self):
        """
        Returns a code identifying the hero's gender.
        
        """
        return self._json_property('gender')
        
    @property
    def create_time(self):
        """
        Return a timestamp for the hero's creation.
        
        """
        return self._json_property('create_time')
        
    @property
    def followers(self):
        """
        Return a dictionary describing the hero's followers.
        
        """
        return self._json_property('followers')
        
    @property
    def active_skills(self):
        """
        Return a dictionary detailing the hero's selectedactive skills.
        
        """
        return self._json_property('skills')['active']
        
    @property
    def passive_skills(self):
        """
        Return a dictionary detailing the hero's selected passive skills.
        
        """
        return self._json_property('skills')['passive']
        
    @property
    def kills(self):
        """
        Return the number of elites killed by the hero.
        
        """
        return self._json_property('kills')
        
    @property
    def stats(self):
        """
        Return a dictionary detailing the character's current stats.
        
        """
        return self._json_property('stats')
