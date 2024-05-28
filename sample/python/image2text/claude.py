import base64
import anthropic

client = anthropic.Anthropic()


# 画像をbase64にエンコードする
def get_base64_encoded_image(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        binary_data = image_file.read()
        base_64_encoded_data = base64.b64encode(binary_data)
        base64_string = base_64_encoded_data.decode("utf-8")
        return base64_string


image_path = "./assets/cat2.jpg"

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    system="必ず日本語で回答してください。",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": get_base64_encoded_image(image_path),
                    },
                },
                {
                    "type": "text",
                    "text": "何が描かれていますか？できる限り詳細に教えてください",
                },
            ],
        }
    ],
)
print(message.content[0].text)
