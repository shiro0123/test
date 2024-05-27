import { GoogleGenerativeAI } from "@google/generative-ai";

const GOOGLE_API_KEY = process.env.GOOGLE_API_KEY;

const main = async () => {
  const genAI = new GoogleGenerativeAI(GOOGLE_API_KEY);
  const model = genAI.getGenerativeModel({ model: "gemini-1.5-pro" });

  const prompt = "こんにちは、芝浦工業大学ShibaLabについて教えてください。";

  const result = await model.generateContentStream(prompt);
  let text = "";
  for await (const chunk of result.stream) {
    const chunkText = chunk.text();
    console.log(chunkText);
    text += chunkText;
  }
};
main();
