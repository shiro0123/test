import os
import google.generativeai as genai

# API-KEYの設定
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

# モデルの選択
# gemini-1.5-flash, gemini-1.5-pro, gemini-1.0-proから選択
model_name = "gemini-1.5-flash"
prompt = "こんにちは"

model = genai.GenerativeModel(model_name)
response = model.generate_content(prompt)
print(response.text)