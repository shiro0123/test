from openai import OpenAI

client = OpenAI()

# modelの選択
# gpt-3.5-turbo, gpt-4, gpt-4oから選択
model_name = "gpt-4o"
prompt="こんにちは"

completion = client.chat.completions.create(
  model=model_name,
  messages=[
    {"role": "system", "content": "あなたはミッキーマウスです。必ず日本語で回答してください。"},
    {"role": "user", "content": prompt}
  ]
)

response = completion.choices[0].message.content
print(response)