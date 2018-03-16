from chatterbot.logic import LogicAdapter
from database import offensive_words

class Greet(LogicAdapter):
    def __init__(self, **kwargs):
        super(Greet, self).__init__(**kwargs)

    def can_process(self, statement):
        words = ['Hi','hello']
        print(statement.text.split())
        if any(x in statement.text.split() for x in words):
            print('true')
            return True
    	else:
        	return False

    def process(self, statement):
        from chatterbot.conversation import Statement
        import random

        # Randomly select a confidence between 0 and 1
        confidence = random.uniform(0, 1)

        # For this example, we will just return the input as output
        selected_statement = Statement('greeted')

        return confidence, selected_statement