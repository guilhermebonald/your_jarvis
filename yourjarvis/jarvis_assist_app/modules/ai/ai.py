import time
import modules.queries as queries
from abc import ABC, abstractmethod


class PoeInterface(ABC):
    @abstractmethod
    def get_chat_id(self, bot: str):
        pass

    @abstractmethod
    def create_chat(self, bot: str = "chinchilla", message: str = ""):
        pass

    @abstractmethod
    def send_msg(self, bot: str, message: str):
        pass

    @abstractmethod
    def get_last_msg(self):
        pass


class PoeAiGen(PoeInterface):
    def __init__(self, request, client, key_cookie):
        self.request = request
        self.client = client
        self.key_cookie = key_cookie

    def get_chat_id(self, bot: str):
        # TODO - Padrão de requisição do GraphQL
        query_data = """
            query ChatViewQuery($bot: String!) {
                chatOfBot(bot: $bot) {
                    id
                    chatId
                    defaultBotNickname
                    shouldShowDisclaimer
                }
            }
        """
        variables = {"bot": bot}
        query = {
            "operationName": "ChatViewQuery",
            "query": query_data,
            "variables": variables,
        }
        response = self.request.DoRequest(self.client, self.key_cookie).main_request(
            json=query
        )
        data = response.get("data")
        return data["chatOfBot"]["chatId"]

    def create_chat(self, bot: str = "chinchilla", message: str = ""):
        variables = {
            "bot": bot,
            "query": message,
            "source": {
                "sourceType": "chat_input",
                "chatInputMetadata": {
                    "useVoiceRecord": False,
                    "newChatContext": "chat_settings_new_chat_button",
                },
            },
            "sdid": "",
            "attachments": [],
        }
        query = queries.query_generate(
            "ChatHelpersSendNewChatMessageMutation", variables
        )
        response = self.request.DoRequest(self.client, self.key_cookie).main_request(
            json=query
        )
        return response["data"]["messageEdgeCreate"]["chat"]

    def send_msg(self, bot: str, message: str):
        chat_id = self.get_chat_id(bot)
        bot_response = []
        variables = {
            "bot": bot,
            "chatId": chat_id,
            "query": message,
            "source": {
                "sourceType": "chat_input",
                "chatInputMetadata": {"useVoiceRecord": False},
            },
            "withChatBreak": False,
            "clientNonce": None,
            "sdid": "",
            "attachments": bot_response,
        }
        query = queries.query_generate("SendMessageMutation", variables)
        response_json = self.request.DoRequest(
            self.client, self.key_cookie
        ).main_request(json=query)
        # message_data = response_json["data"]["messageEdgeCreate"]["chat"]
        # return message_data

    def get_last_msg(self):
        query = """query ChatPaginationQuery($bot: String!, $before: String, $last: Int! = 10) {
                        chatOfBot(bot: $bot) {
                            id
                            __typename
                            messagesConnection(before: $before, last: $last) {
                                pageInfo {
                                    hasPreviousPage
                                }
                                edges {
                                    node {
                                        id
                                        __typename
                                        messageId
                                        text
                                        linkifiedText
                                        authorNickname
                                        state
                                        vote
                                        voteReason
                                        creationTime
                                        suggestedReplies
                                    }
                                }
                            }
                        }
                    }
                """
        variables = {"bot": "chinchilla", "before": None, "last": 1}
        query = {
            "operationName": "ChatPaginationQuery",
            "query": query,
            "variables": variables,
        }
        while True:
            time.sleep(2)
            response = self.request.DoRequest(
                self.client, self.key_cookie
            ).main_request(json=query)
            text = response["data"]["chatOfBot"]["messagesConnection"]["edges"][-1][
                "node"
            ]["text"]
            state = response["data"]["chatOfBot"]["messagesConnection"]["edges"][-1][
                "node"
            ]["state"]
            author_nickname = response["data"]["chatOfBot"]["messagesConnection"][
                "edges"
            ][-1]["node"]["authorNickname"]
            if author_nickname == "chinchilla" and state == "complete":
                break
        return text


# poe_key = getenv("POE-KEY")

# poe = PoeAiGen(request=req, client=Client, key_cookie=poe_key)
# poe.send_msg(
#     bot="chinchilla",
#     message="Esse fenomeno é normal ou acontece por causa do aquecimento global?",
# )
# print(poe.get_last_msg())
