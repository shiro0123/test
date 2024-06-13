import cohere
import os

API_KEY = os.getenv("CO_API_KEY")

co = cohere.Client(API_KEY)

response = co.chat(
    # command-r-plus or command-r
    model="command-r-plus",
    chat_history=[
        {"role": "USER", "message": "日本の首都はどこですか？"},
        {
            "role": "CHATBOT",
            "message": "東京です。",
        },
    ],
    message="では、人口は？",
)

print(response.text)
