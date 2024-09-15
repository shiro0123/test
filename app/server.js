import express from "express";
import path from "path";
import { fileURLToPath } from "url";
import OpenAI from "openai";

const app = express();
const port = 3000;

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

app.use(express.json());
app.use(express.static(__dirname + "/public"));
app.get("/", (req, res) => {
  res.sendFile(__dirname + "/public/index.html");
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});

// ---------------
// 以下にAPIを実装
// ---------------

app.post("/api/hello", async (req, res) => {
  const now = new Date().toLocaleString();
  res.send("こんにちは! 現在時刻は" + now + "です!");
});
