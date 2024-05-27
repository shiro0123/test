import fs from "node:fs";
import axios from "axios";
import FormData from "form-data";

const formData = {
  prompt:
    "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k",
  output_format: "jpeg",
  model: "sd3", // sd3 or sd3-turbo turboは高速で低価格
  mode: "image-to-image",
  strength: 0.6, // 0だと入力画像そのまま、1だと完全に生成画像
  image: fs.createReadStream("./assets/sample.png"),
};

const response = await axios.postForm(
  `https://api.stability.ai/v2beta/stable-image/generate/sd3`,
  axios.toFormData(formData, new FormData()),
  {
    validateStatus: undefined,
    responseType: "arraybuffer",
    headers: {
      Authorization: `Bearer ${process.env.STABILITY_API_KEY}`,
      Accept: "image/*",
    },
  }
);

if (response.status === 200) {
  fs.writeFileSync(
    "./src/javascript/image2image/result.png",
    Buffer.from(response.data)
  );
} else {
  throw new Error(`${response.status}: ${response.data.toString()}`);
}
