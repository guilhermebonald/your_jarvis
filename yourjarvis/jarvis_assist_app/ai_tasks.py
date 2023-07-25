from spacy import load
from spacy.matcher import Matcher

class DoTask:
    def __init__(self):
        self.intentions = []
        self.lemma = []
        self.nlp = load("pt_core_news_lg")

    def get_intention(self, intention=str, patterns=list) -> list:
        matcher = Matcher(self.nlp.vocab)

        matcher.add("DEFAULT_A", [patterns])

        doc = self.nlp("{}".format(intention))

        matches = matcher(doc)

        for match_id, start, end in matches:
            matched = doc[start:end]
            self.intentions.append(matched.text)

        return self.intentions

  
    def get_lemma(self) -> list:
        intention = []
        
        for i in self.intentions:
            intention.append(i)

        for l in intention:
            doc = self.nlp(l)
            for d in doc:
                self.lemma.append(d.lemma_)
        
        return self.lemma
    
    
    def do_reminder(self):
        for l in self.lemma:
            if "criar" and "lembrete" in l:
                print("Lembrete Criado!")


# ONLY FOR EXECUTE TESTS

my_pattern = [
    {"POS": "VERB"},
    {"OP": "?"},
    {"POS": "NOUN"},
]


task = DoTask()
task.get_intention("crie um lembrete para mim", my_pattern)
task.get_lemma()
task.do_reminder()