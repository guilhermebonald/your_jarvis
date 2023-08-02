from spacy import load
from spacy.matcher import Matcher


class IntentProcessing:
    def __init__(self):
        self.intentions = []
        self.nlp = load("pt_core_news_lg")

    def process_intention(self, intention=str, patterns=list) -> list:
        matcher = Matcher(self.nlp.vocab)

        matcher.add("DEFAULT_A", [patterns])

        doc = self.nlp("{}".format(intention))

        matches = matcher(doc)

        for match_id, start, end in matches:
            matched = doc[start:end]
            self.intentions.append(matched.text)

        return self.intentions


class Lemmatizer:
    def __init__(self):
        self.lemma = []
        self.nlp = load("pt_core_news_lg")

    def get_lemma(self, intentions=list) -> list:
        for l in intentions:
            doc = self.nlp(l)
            for token in doc:
                self.lemma.append(token.lemma_)

        return self.lemma