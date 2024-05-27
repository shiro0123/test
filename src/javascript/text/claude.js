import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

const main = async () => {
  const message = await anthropic.messages.create({
    max_tokens: 1024,
    messages: [
      {
        role: "user",
        content: "こんにちは、芝浦工業大学ShibaLabについて教えてください。",
      },
    ],
    model: "claude-3-haiku-20240307",
  });

  console.log(message.content[0].text);
};

main();
