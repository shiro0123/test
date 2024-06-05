import OpenAI from "openai";
import fs from "node:fs";

async function main() {
  const client = new OpenAI(process.env.OPENAI_API_KEY);

  const imagePath = "./assets/techshiba.jpg";
  const imageBuffer = fs.readFileSync(imagePath);
  const base64Image = imageBuffer.toString("base64");

  const completion = await client.chat.completions.create({
    model: "gpt-4o",
    messages: [
      { role: "system", content: "必ず日本語で回答してください。" },
      {
        role: "user",
        content: [
          {
            type: "text",
            text: "写っているキャラクターについて教えてください。",
          },
          {
            type: "image_url",
            image_url: {
              url: `data:image/jpg;base64,${base64Image}`,
            },
          },
        ],
      },
    ],
    n: 1, // 出力の数
    max_tokens: 150, // 出力上限
    temperature: 0.5, // 0.0-1.0
  });

  console.log(completion.choices[0].message.content);
}

main();
