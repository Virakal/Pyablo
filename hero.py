import pyablo

class Hero(pyablo._FetchMixin):
    """
    Encapsulates a Diablo 3 hero.
    
    """
    
    _PATH = 'hero/'
    
    def __init__(self, api, id, region=None, locale=None, json=None):
        """
        
        """
        if not region: region = api.region
        if not locale: locale = api.locale
        self._api = api
        self._id = id
        self._region = region
        self._locale = locale
        self._json = json
        
        self._url = pyablo.REGION[region]['prefix'] + self._PATH + str(id)
        
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
        Returns an ID for the hero's class.
        
        """
        return self._json_property('hero_class')
        
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
    def update_time(self):
        """
        Return a timestamp representing the time the hero was last updated.
        
        """
        return self._json_property('update_time')
        
    @property
    def hirelings(self):
        """
        Return a dictionary describing the hero's hirelings.
        
        """
        return self._json_property('hireling')
        
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
    def elites_killed(self):
        """
        Return the number of elites killed by the hero.
        
        """
        return self._json_property('elites_killed')
        
    @property
    def stats(self):
        """
        Return a dictionary detailing the character's current stats.
        
        """
        return self._json_property('attributes')
