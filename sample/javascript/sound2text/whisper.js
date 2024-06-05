import OpenAI from "openai";
import fs from "node:fs";

// WhisperはLLMではなく、文字起こしAI
// 低価格で高精度なので、ChatGPTやClaudeなどのAIと組み合わせて使うと良い

async function main() {
  const client = new OpenAI(process.env.OPENAI_API_KEY);

  const audioPath = "./assets/midori.mp3";

  const completion = await client.audio.transcriptions.create({
    model: "whisper-1",
    file: fs.createReadStream(audioPath),
    language: "ja",
  });

  console.log(completion.text);
}

main();
