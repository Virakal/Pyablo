__author__ = "Jonathan Goodger (jonno.is@gmail.com) (Jonno#2600)"
__version__ = "0.1a"

__all__ = [
    'D3API', 'Account', 'Hero'
]

#
# Package Imports
#
from pyablo.fetch import _FetchMixin
from pyablo.d3api import D3API
from pyablo.account import Account
from pyablo.hero import Hero

#
# Hide package structure
#
del fetch
del d3api
del account
del hero

#
# Global constants
#
REGION = {
    'eu' : {
        'prefix'  : 'http://eu.battle.net/api/d3/',
        'locales' : ['en_GB', 'es_ES', 'fr_FR', 'ru_RU', 'de_DE']
    },
    'us' : {
        'prefix'  : 'http://us.battle.net/api/d3/',
        'locales' : ['en_US', 'es_MX']
    },
}