import os
import google.generativeai as genai

# API-KEYの設定
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

# ファイルのアップロード
picture = genai.upload_file(
    path="./assets/cat2.jpg",
    display_name="image1",
)

prompt = "画像には何が写っていますか？詳細に説明してください。"

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content([prompt, picture])
print(response.text)
