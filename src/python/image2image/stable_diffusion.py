import requests
import os
from PIL import Image


def get_image_bytes(image_path: str) -> bytes:
    with open(image_path, "rb") as image_file:
        return image_file.read()


API_KEY = os.getenv("STABILITY_API_KEY")

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/sd3",
    headers={
        "authorization": f"Bearer {API_KEY}",
        "accept": "image/*",
    },
    files={"image": get_image_bytes("./assets/sample.png")},
    data={
        "prompt": "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k",  # SDでは英語である必要がある
        "output_format": "png",
        "model": "sd3",  # sd3 or sd3-turbo turboは高速で低価格
        "mode": "image-to-image",
        "strength": 0.6,  # 0だと入力画像そのまま、1だと完全に生成画像
    },
)

if response.status_code == 200:
    with open("./src/python/image2image/sd3_result.jpeg", "wb") as file:
        file.write(response.content)
else:
    raise Exception(str(response.json()))
