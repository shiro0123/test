import os
import google.generativeai as genai
import time

# API-KEYの設定
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

# ファイルのアップロード
video = genai.upload_file(
    path="./assets/midori.mp4",
    display_name="mdr",
)
print(video.name)


# Tips: 動画の解析に時間がかかるので、待機する必要がある
time.sleep(10)

prompt = "動画の様子を教えてください"

# 動画読み込みにflash modelは現状使えないのでproを使う（2024/06/01）
model = genai.GenerativeModel("gemini-1.5-pro")
response = model.generate_content([prompt, video])
print(response.text)

genai.delete_file(video.name)
