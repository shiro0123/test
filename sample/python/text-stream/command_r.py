import cohere
import os

API_KEY = os.getenv("CO_API_KEY")

co = cohere.Client(API_KEY)

response = co.chat_stream(
    message="こんにちは、芝浦工業大学ShibaLabについて教えてください。",
    # ウェブ検索の結果を含めることができる
    connectors=[{"id": "web-search"}],
)

for event in response:
    if event.event_type == "text-generation":
        print(event.text, end="")
