from openai import OpenAI

client = OpenAI()
response = client.images.generate(
    model="dall-e-3",  # モデル dall-e-2 or dall-e-3
    prompt="芝浦工業大学熱海セミナーハウス",  # プロンプト
    n=1,  # 生成数
    size="1024x1024",  # 解像度 dall-e-3では1024x1024、1792x1024、1024x1792
    response_format="url",  # レスポンスフォーマット url or b64_json
    quality="standard",  # hdは価格が高いので今回はstandard固定
    style="vivid",  # スタイル vivid or natural
)

# Tips: URLは2時間程度で無効になる
print(response.data[0].url)
