from openai import OpenAI

client = OpenAI()

# modelの選択
# gpt-3.5-turbo, gpt-4, gpt-4oから選択
model_name = "gpt-3.5-turbo"
prompt = "こんにちは、芝浦工業大学ShibaLabについて教えてください。"

completion = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "system", "content": "必ず日本語で回答してください。"},
        {"role": "user", "content": prompt},
    ],
    n=1,  # 出力の数
    max_tokens=150,  # 出力上限（4096まで）
    temperature=0.5,  # 0.0-1.0
)

response = completion.choices[0].message.content
print(response)
