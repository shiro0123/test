from openai import OpenAI
import base64

client = OpenAI()


# 画像をbase64にエンコードする
def get_base64_encoded_image(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        binary_data = image_file.read()
        base_64_encoded_data = base64.b64encode(binary_data)
        base64_string = base_64_encoded_data.decode("utf-8")
        return base64_string


# modelの選択
# gpt-3.5-turbo, gpt-4, gpt-4oから選択
model_name = "gpt-4o"

image_path = "./assets/techshiba.jpg"

completion = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "system", "content": "必ず日本語で回答してください。"},
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "写っているキャラクターについて教えてください。",
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "data:image/jpg;base64,"
                        + get_base64_encoded_image(image_path)
                    },
                },
            ],
        },
    ],
)

response = completion.choices[0].message.content
print(response)
