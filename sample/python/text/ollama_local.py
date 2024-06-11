import ollama


response = ollama.chat(
    model="qwen",
    messages=[
        {
            "role": "system",
            "content": "Use Japanese",
        },
        {
            "role": "user",
            "content": "Why is the sky blue?",
        },
    ],
)
print(response["message"]["content"])
