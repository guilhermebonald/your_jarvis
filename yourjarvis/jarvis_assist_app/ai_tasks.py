from spacy import load
from spacy.matcher import Matcher

nlp = load("pt_core_news_lg")


class DoTask:
    def __init__(self):
        self.intentions = []

    def get_intention(self, intention=str, patterns=list) -> list:
        matcher = Matcher(nlp.vocab)

        matcher.add("DEFAULT_A", [patterns])

        doc = nlp("{}".format(intention))

        matches = matcher(doc)

        for match_id, start, end in matches:
            matched = doc[start:end]
            self.intentions.append(matched.text)

        return self.intentions

    def create_reminder(self):
        intention = self.get_intention()
        for i in intention:
            print(i)



# ONLY FOR EXECUTE TESTS

my_pattern = [
    {"POS": "VERB"},
    {"OP": "?"},
    {"POS": "NOUN"},
]


task = DoTask()
print(task.get_intention("Crie um lembrete para mim", my_pattern))