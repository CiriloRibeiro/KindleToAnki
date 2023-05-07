from KindleToAnki import KindleToAnki
from DeckCreator import DeckCreator

API_KEY = "644443cb-bbc4-4d01-9884-bae3d87d2419"

def initialize(API_KEY):
    
    vocab = KindleToAnki(API_KEY)
    print(vocab.getTitle())
    while True:
        try:
            ID = input("\nSelect a valid Title ID, or q to quit: ")
            if ID == "q":
                exit()
            ID = int(ID)
            if ID < vocab.df['id'].min() or ID > vocab.df['id'].max():
                raise ValueError(f"ID must be between {vocab.df['id'].min()} and {vocab.df['id'].max()}")
            break
        except ValueError as error:
            print(error)

    print(vocab.setTitleById(ID))
    #print(vocab.df.head())
    #Alternativaly, you can set title by name, e.g: vocab.setTitleByName("The Power of Habit")
    vocab.createDefinitionColumn()
    deck = DeckCreator(vocab.getSelectedTitle())
    # Create cards for each row in the dataframe
    deck.addCard(vocab.df['stem'], vocab.df['definition'], vocab.df['usage'])
    print(deck.saveDeck())

if __name__ == "__main__":
    initialize(API_KEY)

        