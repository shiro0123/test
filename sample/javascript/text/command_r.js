import { CohereClient } from "cohere-ai";

const cohere = new CohereClient({
  token: process.env.CO_API_KEY,
});

async function main() {
  const response = await cohere.chat({
    chatHistory: [
      { role: "USER", message: "Who discovered gravity?" },
      {
        role: "CHATBOT",
        message:
          "The man who is widely credited with discovering gravity is Sir Isaac Newton",
      },
    ],
    message: "What year was he born?",
    // Web検索を有効にする
    connectors: [{ id: "web-search" }],
  });

  console.log(response.text);
}

main();
