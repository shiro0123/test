import p5 from "p5";

// ボタンを押した時の動作
document.getElementById("button").addEventListener("click", async () => {
  const response = await fetch("/api/hello", {
    method: "POST",
  });
  const text = await response.text();
  document.getElementById("hello").textContent = text;
});

// p5.jsのスケッチ
function sketch(p) {
  // 最初に1回だけ実行される
  p.setup = () => {
    p.createCanvas(window.innerWidth, window.innerHeight);
    p.noStroke();
  };

  // 1フレームごとに実行される
  p.draw = () => {
    p.background(220);
    p.fill(196, 196, 255);
    p.ellipse(p.mouseX, p.mouseY, 50, 50);
  };
}

new p5(sketch, "p5canvas");
