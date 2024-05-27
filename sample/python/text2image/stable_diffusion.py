import requests
import os

API_KEY = os.getenv("STABILITY_API_KEY")

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/sd3",
    headers={
        "authorization": f"Bearer {API_KEY}",
        "accept": "image/*",
    },
    files={"none": ""},
    data={
        "prompt": "a cat on a skateboard",  # SDでは英語である必要がある
        "output_format": "jpeg",
        "model": "sd3",  # sd3 or sd3-turbo turboは高速で低価格
        "aspect_ratio": "1:1",  # 16:9 1:1 21:9 2:3 3:2 4:5 5:4 9:16 9:21
    },
)

if response.status_code == 200:
    with open("./src/python/text2image/sd3_result.jpeg", "wb") as file:
        file.write(response.content)
else:
    raise Exception(str(response.json()))
