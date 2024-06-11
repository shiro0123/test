import ollama

stream = ollama.chat(
    model="qwen2",
    messages=[
        {
            "role": "system",
            "content": "Use Japanese",
        },
        {"role": "user", "content": "Why is the sky blue?"},
    ],
    stream=True,
)

for chunk in stream:
    print(chunk["message"]["content"], end="", flush=True)
