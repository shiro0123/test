from openai import OpenAI

# WhisperはLLMではなく、文字起こしAI
# 低価格で高精度なので、ChatGPTやClaudeなどのAIと組み合わせて使うと良い

audio_file = open("./assets/midori.mp3", "rb")

client = OpenAI()

transcription = client.audio.transcriptions.create(
    file=audio_file,
    model="whisper-1",
)

print(transcription.text)
