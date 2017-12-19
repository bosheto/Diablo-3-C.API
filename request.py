import sys
from urllib.request import urlopen as uOpen
import ujson

class API:
    '''API object'''
    API_KEY = ''
    LOCALE = ''

    def __init__(self, api_key, locale):
        self.API_KEY = api_key
        self.LOCALE = locale
    
    def get_career_profile(self, battleTag):
        '''Get career profile'''
        battleTag = str(battleTag).replace('#', '%23')
        url = 'https://eu.api.battle.net/d3/profile/{}/?locale={}&apikey={}'.format(battleTag,self.LOCALE, self.API_KEY)
        uClient = uOpen(url)
        output = uClient.read()
        uClient.close()
        parsed_output = ujson.loads(output)

        return parsed_output

    def get_hero_profile(self,battleTag,heroID):
        '''Get hero profile'''
        battleTag = str(battleTag).replace('#', '%23')
        url = 'https://eu.api.battle.net/d3/profile/{}/hero/{}?{}&apikey={}'.format(battleTag, heroID, self.LOCALE, self.API_KEY)
        uClient = uOpen(url)
        output = uClient.read()
        uClient.close()
        parsed_output = ujson.loads(output)

        return parsed_output
    
    def get_item_data(self, item_data):
        '''Get item data'''
        url = 'https://eu.api.battle.net/d3/data/item/{}?locale={}&apikey={}'.format(item_data, self.LOCALE, self.API_KEY)
        uClient = uOpen(url)
        output = uClient.read()
        uClient.close()
        parsed_output = ujson.loads(output)

        return parsed_output