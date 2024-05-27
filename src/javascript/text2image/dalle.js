import OpenAI from "openai";

const main = async () => {
  const client = new OpenAI(process.env.OPENAI_API_KEY);

  const prompt = "芝浦工業大学熱海セミナーハウス";
  const result = await client.images.generate({
    model: "dall-e-3",
    prompt: prompt,
    n: 1, // 出力の数
    size: "1024x1024",
    response_format: "url",
    quality: "standard",
  });

  console.log(result.data[0].url);
};

main();
