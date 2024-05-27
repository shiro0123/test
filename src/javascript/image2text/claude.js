import Anthropic from "@anthropic-ai/sdk";
import fs from "node:fs";

const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

const main = async () => {
  const imagePath = "./assets/techshiba.jpg";
  const imageBuffer = fs.readFileSync(imagePath);
  const base64Image = imageBuffer.toString("base64");

  const message = await anthropic.messages.create({
    max_tokens: 1024,
    system: "日本語で回答してください。",
    messages: [
      {
        role: "user",
        content: [
          {
            type: "image",
            source: {
              type: "base64",
              media_type: "image/jpeg",
              data: base64Image,
            },
          },
          {
            type: "text",
            text: "何が描かれていますか？できる限り詳細に教えてください",
          },
        ],
      },
    ],
    model: "claude-3-haiku-20240307",
  });

  console.log(message.content[0].text);
};

main();
