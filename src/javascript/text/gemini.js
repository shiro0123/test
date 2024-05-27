import { GoogleGenerativeAI } from "@google/generative-ai";

const GOOGLE_API_KEY = process.env.GOOGLE_API_KEY;

const main = async () => {
  const genAI = new GoogleGenerativeAI(GOOGLE_API_KEY);
  const model = genAI.getGenerativeModel({ model: "gemini-1.5-pro" });

  const prompt = "こんにちは、芝浦工業大学ShibaLabについて教えてください。";

  const result = await model.generateContent(prompt);

  console.log(result.response.text());
};
main();
