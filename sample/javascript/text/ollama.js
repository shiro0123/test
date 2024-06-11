import ollama from "ollama";

const response = await ollama.chat({
  model: "qwen2",
  messages: [
    { role: "system", content: "Use Japanese" },
    { role: "user", content: "こんにちは、あなたについて教えてください" },
  ],
});
console.log(response.message.content);
