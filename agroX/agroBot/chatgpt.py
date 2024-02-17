import requests

class ChatGPT:
    def __init__(self, api_key):
        self.api_key = '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'
        self.endpoint = "https://api.openai.com/v1/chat/completions"

    def generate_response(self, message):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
        data = {
            "model": "text-davinci-003",
            "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": message}],
        }
        response = requests.post(self.endpoint, headers=headers, json=data)
        return response.json()["choices"][0]["message"]["content"]