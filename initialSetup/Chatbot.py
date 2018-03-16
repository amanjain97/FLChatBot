from chatterbot import ChatBot
from chatterbot.comparisons import levenshtein_distance
# from chatterbot.trainers import ChatterBotCorpusTrainer

class ChatbotSetup:
    def __init__(self,database = 'jarvii-database',**kwargs):
        self.Jarvii = ChatBot("English Bot",
            storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
            filters=["chatterbot.filters.RepetitiveResponseFilter"],
            logic_adapters=[
                {
                'import_path': 'LogicAdapters.RemoveOffensiveWords',
                "response_selection_method": "chatterbot.comparisons.levenshtein_distance"
                },
                {
                'import_path': 'LogicAdapters.Greet',
                "response_selection_method": "chatterbot.comparisons.levenshtein_distance"
                },
                {
                "import_path": "chatterbot.logic.BestMatch",
                "response_selection_method": "chatterbot.comparisons.levenshtein_distance",
                "statement_comparison_function": "chatterbot.response_selection.get_first_response"
                },
                {
                "import_path": "chatterbot.logic.TimeLogicAdapter"
                },
                {
                "import_path":"chatterbot.logic.MathematicalEvaluation"
                },
                {
                'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                'input_text': 'What can you do?',
                'output_text': 'Hi, I can deal with time and maths right now(Still learning though) please do not be offensive with me, have a nice day :)'
                }   
            ],
        database = database,
        )
        # self.Jarvii.set_trainer(ChatterBotCorpusTrainer)
        # self.Jarvii.train(
        # "chatterbot.corpus.english"
        # )

        

    def getResponse(self,message):
        return str(self.Jarvii.get_response(message))
