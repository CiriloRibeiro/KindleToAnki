import genanki, random, os

class DeckCreator:
    def __init__(self, deckName):
            self.model_id = random.randrange(1 << 30, 1 << 31)
            self.deck_id = random.randrange(1 << 30, 1 << 31)
            self.deckName = deckName
            self.cardNumber = 1
            self.model = genanki.Model(self.model_id ,
            self.deckName,
            fields=[
                {'name': 'Question'},
                {'name': 'Answer'},
                {'name': 'Example'}
            ],
            templates=[
                {
                    'name': 'Card {{self.cardNumber}}',
                    'qfmt': '<h1 style="text-align:center;color:#a6ff4d;font-weight: normal;">{{Question}}</h1>',
                    'afmt': '<h1 style="text-align:center;color:#a6ff4d;font-weight: normal;">{{Question}}</h1><br><hr id="answer"><h1 style="text-align:center; text-align:justify;color:#4dffff;font-weight: normal;">Definition: {{Answer}}</h1><br><h1 style="text-align:center; text-align:justify;color:#ff4d4d;font-weight: normal;">Example: {{Example}}</h1>',
                },
                ]   
            )

    def addCard(self, questions, answers, examples):
        try:
            self.deck = genanki.Deck(self.deck_id, self.deckName)
            for question, answer, example in zip(questions, answers, examples):
                self.cardNumber += 1
                self.note = genanki.Note(
                    model=self.model,
                    fields=[f'{question}', f'{answer}', f'{example}'])
                self.deck.add_note(self.note)
        except Exception as e:
            print(e)

    def saveDeck(self):
        try:
            dir_name = "Decks"
            if not os.path.exists(dir_name):
                os.mkdir(dir_name)
            anki_folder = os.path.abspath(dir_name)
           # anki_folder = os.getcwd()
            anki_questions_file = os.path.join(anki_folder, f"{self.deckName}_vocab_deck.apkg")
            

            genanki.Package(self.deck).write_to_file(anki_questions_file)
            return "Deck saved successfully."
        except Exception as e:
            print(e)
