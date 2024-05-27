import fs from "node:fs";
import axios from "axios";
import FormData from "form-data";

const formData = {
  prompt: "Lighthouse on a cliff overlooking the ocean",
  output_format: "jpeg",
  model: "sd3", // sd3 or sd3-turbo turboは高速で低価格
  aspect_ratio: "1:1", // 16:9 1:1 21:9 2:3 3:2 4:5 5:4 9:16 9:21
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
    "./src/javascript/text2image/lighthouse.jpeg",
    Buffer.from(response.data)
  );
} else {
  throw new Error(`${response.status}: ${response.data.toString()}`);
}
