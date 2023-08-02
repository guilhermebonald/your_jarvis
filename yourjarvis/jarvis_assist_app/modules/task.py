from abc import ABC, abstractmethod
from lang_process import IntentProcessing, Lemmatizer


class DoTask(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass        
     

class CreateReminder(DoTask):
    def __init__(self, lemma=list) -> None:
        self.lemma = lemma

    def execute(self) -> None:
        for i in self.lemma:
            if "criar" and "lembrete" in i:
                print("Lembrete criado!")



# ? ONLY FOR EXECUTE TESTS

my_pattern = [
    {"POS": "VERB"},
    {"OP": "?"},
    {"POS": "NOUN"},
]

intent_process = IntentProcessing()
intentions = intent_process.process_intention("Criar lembrete", my_pattern)

lemma_process = Lemmatizer()
lemma = lemma_process.get_lemma(intentions)

create_r = CreateReminder(lemma=lemma)
create_r.execute()