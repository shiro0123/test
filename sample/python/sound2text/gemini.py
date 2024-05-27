import os
import google.generativeai as genai

# API-KEYの設定
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

# ファイルのアップロード
picture = genai.upload_file(
    path="./assets/midori.mp3",
    display_name="sound1",
)

prompt = "これは何についてしゃべっていますか？"

# 動画読み込みにflash modelは現状使えないのでproを使う（2024/06/01）
model = genai.GenerativeModel("gemini-1.5-pro")
response = model.generate_content([prompt, picture])
print(response.text)
