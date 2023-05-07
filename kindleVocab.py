import os
import sqlite3
import pandas as pd

pd.set_option('mode.chained_assignment', None) 

class kindleVocab(object):
    '''This class fetches the vocabulary of a book from the Kindle database.'''
    def __init__(self):
        '''
        Connects to the database and create a DataFrame.
        '''

        self.SQLCode = '''SELECT w.stem, w.word, w.lang, w.id, l.usage, l.book_key, b.title, b.authors
        FROM WORDS w
        JOIN LOOKUPS l ON w.id = l.word_key
        JOIN BOOK_INFO b ON l.book_key = b.id;
        '''

        try:
            #get path
            file_path = self.getPath()
            #open database
            self.db = sqlite3.connect(file_path)
            #create a dataframe
            self.df = self.createDataframe(self.SQLCode, self.db)
            print("\nDatabase connection opened and DataFrame created\n")
            self.db.close()
        except sqlite3.Error as e:
            print(e)
            print("Database connection failed")
    
    def getPath(self):
        '''Gets the path to the vocab.db file'''
        try:
            # Get the current working directory
            cwd = os.getcwd()
            # Specify the name of the file you want to find the path for
            filename = "vocab.db"
            # Use os.path.join() to construct the full path to the file
            file_path = os.path.join(cwd, filename)
            return file_path
        except:
            return "vocab.db does not exist. Please add it to the same directory as this script."
    
    def createDataframe(self, SQLCode, db):
        '''Creates and filters the dataframe'''
        sql_query = pd.read_sql_query(SQLCode,db)
        sql_query = sql_query.drop('book_key', axis=1)
        sql_query = sql_query.drop('id', axis=1)
        sql_query = sql_query.sort_values(by='title')
        unique_titles = sorted(set(sql_query['title']))
        title_to_id = {title: i+1 for i, title in enumerate(unique_titles)}
        sql_query.reset_index(drop=True, inplace=True)
        # add a new column with the id for each title
        sql_query['id'] = sql_query['title'].apply(lambda x: title_to_id[x])
        sql_query['stem'] = sql_query['stem'].str.capitalize()
        self.isTitleSet = False
        return sql_query
        
    def getLanguage(self):
        '''Gets unique languages'''
        return self.df["lang"].unique()

    def setLanguage(self, lang):
        '''Sets the language and drops unused columns'''
        self.lang = lang
        self.df = self.df[self.df["lang"] == self.lang]
        self.df = self.df.drop('lang', axis=1)
        self.df = self.df.drop('word', axis=1)
        return (f"Language set to {self.lang}")
    
    def getTitle(self):
        '''Gets unique book titles'''
        query = pd.DataFrame({'id': self.df['id'].unique(), 'title': self.df['title'].unique()})
        query = query.set_index('id')
        return query

    def isTitle(self, title):
        '''Checks if the title is in the DataFrame'''
        if self.df['title'][self.df['title'] == title].unique() == title:
            return True
        else:
            return False
    
    def isId(self, id):
        '''Checks if the id is in the DataFrame'''
        if self.df['id'][self.df['id'] == id].unique() == id:
            return True
        else:
            return False
    
    def setTitleByName(self, title):
        if not self.isTitleSet:
            if self.isTitle(title):
                self.df = self.df[self.df["title"] == title]
                self.df.reset_index(drop=True, inplace=True)
                self.isTitleSet = True
                return (f"Title set to {self.getSelectedTitle()()}")
            else:
                return "Invalid title, please try again"
        else:
            return "Title already set"

    def setTitleById(self, id):
        if self.isId(id):
            self.df = self.df[self.df["id"] == id]
            self.df.reset_index(drop=True, inplace=True)
            self.isTitleSet = True
            return (f"Title set to {self.getSelectedTitle()}")
        else:
            return "Invalid title, please try again"
    
    def getSelectedTitle(self):
        return self.df["title"].unique()[0]

    def getSelectedAuthor(self):
        return self.df["authors"].unique()[0]

    def getAuthor(self):
        '''Gets unique book authors'''
        return self.df["authors"].unique()

    def getShape(self):
        '''Gets the shape of the DataFrame'''
        return self.df.shape

    def findTitle(self, substring):
        result = self.df[self.df['title'].str.contains(substring, case=False)]
        if not result.empty:
            query = pd.DataFrame({'id': result['id'].unique(), 'title': result['title'].unique()})
            query = query.set_index('id')
            return query
        else:
            return None
    
