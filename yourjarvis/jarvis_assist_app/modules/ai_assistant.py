from abc import ABC, abstractmethod
import requests


class RequestService(ABC):
    """Classe que cria uma interface para o modelo de requisição.

    As classe que herdam essa interface devem implementar o método
    get_api.
    """

    @abstractmethod
    def get_api(self, url: str):
        pass


class HttpClient(RequestService):
    """Classe que efetuará a requisição.

    Recebe uma "url" do tipo "str".
    Retorna um tipo "requests.Response".
    """

    def get_api(self, url: str) -> requests.Response:
        response = requests.get(url)
        return response


class AIAssistant:
    def __init__(self, api_key, request_service):
        self.api_key = api_key
        self.request_service = request_service

    def get_ai_response(self, message):
        url = f"https://api.betterapi.net/youchat?inputs={message}. Responda em portugues&key={self.api_key}"

        response = self.request_service.get_api(url)
        if response.status_code == 200:
            json = response.json()
            return json["generated_text"]
        else:
            return {"Falha na requisição": response.status_code}
