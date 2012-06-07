# Imports
import urllib.request
# from urllib.error import HTTPError, URLError # Not done error checking
import json as jsonlib

# Package Imports
import pyablo

class D3API(pyablo._FetchMixin):
    """
    Encapsulates a connection to the Diablo 3 community platform API servers.
    
    """
    @staticmethod
    def _locale_case(s):
        """
        Convert the passed locale string to normal locale case.
        
        e.g.
        "en_gb" becomes:
            "en_GB"
            
        "EN_US" becomes:
            "en_US"
        
        """
        if not s: return ''
        lang, dialect = tuple(s.split('_'))
        return lang.lower() + '_' + dialect.upper()
        
    def __init__(self, region='us', locale='', private_key=None,
                 public_key=None):
        """
        Create a new D3API connection.
        
        Optional Arguments:
        region -- the server region (default 'us')
        locale -- the locale to use (default '')
        private_key -- your private API key (default None)
        public_key -- your public API key (default None)
        
        """
        self._region = region.lower()
        self._locale = self._locale_case(locale)
        
        
    def _get_json(self, url):
        """Make a dictionary from the JSON file at `url`"""
        # TODO Error checking, from urllib and external
        # TODO Implement API keys here
        req = urllib.request.urlopen(url)
        return jsonlib.loads(str(req.read(), 'UTF-8'))
        
    @property
    def region(self):
        """Return the API's region code"""
        return self._region
        
    @property
    def locale(self):
        """"""
        
    def get_account(self, name, region=None, locale=None):
        """
        Get the account specified in `name`.
        
        `name` should be in the form: 'Battletag#1234'
        
        """
        return pyablo.Account(self, name, region=region, locale=locale)
        
    def get_hero(self, id, region=None, locale=None):
        """
        Ge the hero with the id `id`.
        
        """
        return pyablo.Hero(self, id, region=region, locale=locale)