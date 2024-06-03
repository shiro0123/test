from openai import OpenAI

# OpenAIのAPIキーを設定
client = OpenAI()

# 初期テキスト
input_text = "ある日私が大学で授業を受けていると"

# 生成するトークンの数
num_generate = 100

# 最終的なJSONを保存する場所
result = []

# トークンを連続的に生成
generated_text = input_text
for _ in range(num_generate):
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=generated_text,
        max_tokens=1,
        n=1,
        stop=None,
        temperature=0.6,
        logprobs=10,
    )

    # 生成されたトークンと確率を取得
    next_token = response.choices[0].text
    logprobs = response.choices[0].logprobs.top_logprobs[0]

    generated_text += next_token

    # トークンと確率を表示
    print(f"{next_token}")

    probs = []
    # トップ10のトークンと確率を表示
    for token, prob in logprobs.items():
        probs.append({"token": token, "prob": prob})
        print(f"  {token}, {(prob*100):.4f}%")

    result.append({"next_token": next_token, "probs": probs})

print(result)
print("Generated text:", generated_text)
