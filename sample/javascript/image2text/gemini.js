import { GoogleGenerativeAI } from "@google/generative-ai";
import fs from "node:fs";

const GOOGLE_API_KEY = process.env.GOOGLE_API_KEY;

// URLからbase64エンコードされた文字列を取得します。
async function urlToGenerativePart(url, mimeType) {
  const response = await fetch(url);
  const arrayBuffer = await response.arrayBuffer();
  return {
    inlineData: {
      data: Buffer.from(arrayBuffer).toString("base64"),
      mimeType,
    },
  };
}

// ローカルファイル情報を GoogleGenerativeAI.Part オブジェクトに変換します。
function fileToGenerativePart(path, mimeType) {
  return {
    inlineData: {
      data: Buffer.from(fs.readFileSync(path)).toString("base64"),
      mimeType,
    },
  };
}

async function main() {
  const genAI = new GoogleGenerativeAI(GOOGLE_API_KEY);
  const model = genAI.getGenerativeModel({ model: "gemini-1.5-pro" });

  const prompt = "画像には何が写っていますか？";

  const imageParts = [
    fileToGenerativePart("./assets/techshiba.jpg", "image/jpg"),
  ];

  const result = await model.generateContent([prompt, ...imageParts]);

  console.log(result.response.text());
}
main();
