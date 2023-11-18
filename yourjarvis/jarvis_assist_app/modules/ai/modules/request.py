from re import search
from abc import ABC, abstractmethod


class RequestInterface(ABC):
    @abstractmethod
    def get_formkey(self):
        pass

    @abstractmethod
    def main_request(self, json: dict):
        pass


class DoRequest(RequestInterface):
    URL_BASE = "https://pt.quora.com"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Sec-Ch-Ua": '"Not.A/Brand";v="8", "Chromium";v="112"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Linux"',
        "Upgrade-Insecure-Requests": "1",
    }
    FORMKEY_PATTERN = r'formkey": "(.*?)"'

    def __init__(self, client, cookie):
        self.client = client(base_url=self.URL_BASE, timeout=5)
        self.client.cookies.set("m-b", cookie)
        self.client.headers.update(
            {
                **self.HEADERS,
                "Quora-Formkey": self.get_formkey(),  # FormKey é gerado dinamicamente cada vez que a página é solicitada.
            }
        )

    def get_formkey(self):
        # Captura o código fonte da página e coleta e faz uma busca pelo FormKey
        response = self.client.get(
            self.URL_BASE, headers=self.HEADERS, follow_redirects=True
        )
        formkey = search(self.FORMKEY_PATTERN, response.text)[1]
        return formkey

    def main_request(self, json: dict):
        response = self.client.post(url=f"{self.URL_BASE}/poe_api/gql_POST", json=json)
        if response.status_code == 200 and response.json()["data"] is not None:
            return response.json()
        raise RuntimeError(
            f"ERROR OCURRED: {response.json()['errors'][0]['message']} // STATUS CODE: {response.status_code}"
        )
