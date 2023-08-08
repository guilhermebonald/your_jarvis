from abc import ABC, abstractmethod
from lang_process import IntentProcessing, Lemmatizer


class DoTask(ABC):
    @abstractmethod
    def execute(self, lemma=list) -> None:
        pass


class CreateTasks(DoTask):
    def execute(self, lemma) -> None:
        for i in lemma:
            if "criar" and "lembrete" in i:
                print("Lembrete criado!")
            elif "criar" and "nota" in i:
                print("Nota criada!")


# ? ONLY FOR EXECUTE TESTS

my_pattern = [
    {"POS": "VERB"},
    {"OP": "?"},
    {"POS": "NOUN"},
]

intent_process = IntentProcessing()
intentions = intent_process.process_intention("Criar notas", my_pattern)

lemma_process = Lemmatizer()
lemma = lemma_process.get_lemma(intentions)

create_n = CreateTasks()
create_n.execute(lemma=lemma)