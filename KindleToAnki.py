from kindleVocab import kindleVocab
from EnglishDictionaryAPI import DictionaryAPI
from DeckCreator import DeckCreator

class KindleToAnki(kindleVocab, DictionaryAPI):
    '''A Class that inherits from kindleVocab and DictionaryAPI 
    to create a flashcards deck from a Kindle's vocabulary database.
    '''
    def __init__(self, api_key):
        kindleVocab.__init__(self)
        DictionaryAPI.__init__(self, api_key)
        self.setLanguage("en")
        self.df_copy = self.df
        self.request_counter = 0

    def getWordDefinitions(self, word):
        self.request_counter += 1
        if self.request_counter % 10 == 0:
            print(f"Getting word definitions: Word {self.request_counter} out of {self.getShape()[0]}. This may take a while, please wait...")
        return self.getWordDefinition(word)

    def createDefinitionColumn(self):
        if self.isTitleSet:
            ###slice the df here if you want to check if the API is working properly
            word_definitions = self.df.loc[:,"stem"].apply(self.getWordDefinitions).copy()
            self.df.loc[:, "definition"] = word_definitions
            self.df = self.df.loc[self.df.loc[:,"definition"] != "No definition found"].copy()
            print("Completed definition column")
            return self.df.head()
        else:
            return "Please select a book by calling setTitle"


    
    def resetDataFrame(self):  
        '''Resets the DataFrame'''
        self.df = self.df_copy
        return "DataFrame reset"



