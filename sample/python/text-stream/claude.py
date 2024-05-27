import anthropic

client = anthropic.Anthropic()

# モデルの選択
# claude-3-opus-20240229, claude-3-sonnet-20240229, claude-3-haiku-20240307

model = "claude-3-haiku-20240307"

with client.messages.stream(
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
) as stream:
    for chunk in stream.text_stream:
        print(chunk, end="")

print("")
