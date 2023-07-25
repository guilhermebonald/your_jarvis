import requests

# * Get AI Response from API.
class AIClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_ai_response(self, message):
        url = f"https://api.betterapi.net/youchat?inputs={message}. Responda em portugues&key={self.api_key}"

        response = requests.get(url)
        if response.status_code == 200:
            json = response.json()
            return json["generated_text"]
        else:
            return {"Falha na requisição": response.status_code}

print(AIClient("INKDZOVRYIHBXE0WLSQW0OVT3JCQYAFXBAV").get_ai_response("Ola, boa tarde"))


# ! API fora do ar. Precisa ser alterada!