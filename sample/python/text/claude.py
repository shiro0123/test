import anthropic

client = anthropic.Anthropic()

# モデルの選択
# claude-3-opus-20240229, claude-3-sonnet-20240229, claude-3-haiku-20240307
# claude-3-5-sonnet-20240620

model = "claude-3-5-sonnet-20240620"

message = client.messages.create(
    model=model,
    max_tokens=1000,  # 出力上限
    temperature=0.0,  # 0.0-1.0
    system="",  # 必要ならシステムプロンプトを設定
    messages=[
        {
            "role": "user",
            "content": "こんにちは、芝浦工業大学ShibaLabについて教えてください。",
        }
    ],
)

print(message.content[0].text)
