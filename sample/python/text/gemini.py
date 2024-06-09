import os
import google.generativeai as genai

# API-KEYの設定
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

# モデルの選択
# gemini-1.5-flash, gemini-1.5-pro, gemini-1.0-proから選択
model_name = "gemini-1.5-pro"
prompt = "こんにちは、芝浦工業大学ShibaLabについて教えてください。"

config = {
    "temperature": 0.9,  # 生成するテキストのランダム性を制御
    "top_p": 1,  # 生成に使用するトークンの累積確率を制御
    "top_k": 1,  # 生成に使用するトップkトークンを制御
    "max_output_tokens": 512,  # 最大出力トークン数を指定`
}

model = genai.GenerativeModel(
    model_name,
    generation_config=config,
    system_instruction=[  # System
        "Use Japanese for response.",
    ],
)
response = model.generate_content(prompt)
print(response.text)
