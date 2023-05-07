import requests

class DictionaryAPI(object):
    '''A class for connecting with the Merriam-Webster's Collegiate® Thesaurus API.
    You must have Merriam-Webster's Collegiate® Thesaurus API key to correctly use this class.
    '''
    def __init__(self, api_key):
        self.api_key = api_key

    def getAPIKey(self):
        '''Get the API key'''
        return self.api_key
    
    def setAPIKey(self, api_key):
        '''Set the API key'''
        self.api_key = api_key
    
    def getWordDefinition(self, word):
        '''Makes a GET request to the Merriam-Webster's API and returns the definition of a word
        
        Args:
            word (str): The word to get the definition of
            
        Returns
            definition (str): The definition of the word

        You can verify your requests at https://dictionaryapi.com/account/usage-reports
        '''
        # Make the API request
        response = requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={self.api_key}")
        # Check if the response contains a definition
        if response.json() and len(response.json()) > 0 and "shortdef" in response.json()[0]:
            try:
                definition = response.json()[0]["shortdef"][0].capitalize() + "."
                return definition
            except:
                return "No definition found"
        else:
            return "No definition found"
    