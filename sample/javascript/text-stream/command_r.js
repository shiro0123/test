import { CohereClient } from "cohere-ai";

const cohere = new CohereClient({
  token: process.env.CO_API_KEY,
});

(async () => {
  const chatStream = await cohere.chatStream({
    chatHistory: [
      { role: "USER", message: "Who discovered gravity?" },
      {
        role: "CHATBOT",
        message:
          "The man who is widely credited with discovering gravity is Sir Isaac Newton",
      },
    ],
    message: "What year was he born?",
  });

  for await (const message of chatStream) {
    if (message.eventType === "text-generation") {
      process.stdout.write(message);
    }
  }
})();
