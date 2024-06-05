import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

async function main() {
  const stream = await anthropic.messages
    .stream({
      max_tokens: 1024,
      messages: [
        {
          role: "user",
          content: "こんにちは、芝浦工業大学ShibaLabについて教えてください。",
        },
      ],
      model: "claude-3-haiku-20240307",
    })
    .on("text", (text) => {
      console.log(text);
    });

  const message = await stream.finalMessage();
  console.log(message);
}

main();
