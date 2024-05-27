import OpenAI from "openai";

const main = async () => {
  const client = new OpenAI(process.env.OPENAI_API_KEY);

  const prompt = "こんにちは、芝浦工業大学ShibaLabについて教えてください。";
  const stream = await client.chat.completions.create({
    model: "gpt-3.5-turbo",
    stream: true,
    messages: [
      { role: "system", content: "必ず日本語で回答してください。" },
      { role: "user", content: prompt },
    ],
    n: 1, // 出力の数
    max_tokens: 150, // 出力上限
    temperature: 0.5, // 0.0-1.0
  });

  for await (const message of stream) {
    const token = message.choices[0].delta.content;
    if (token) {
      console.log(token);
    }
  }
};

main();
