document.getElementById("button").addEventListener("click", () => {
  fetch("/api/hello", {
    method: "POST",
  })
    .then((response) => response.text())
    .then((text) => {
      document.getElementById("hello").textContent = text;
    });
});
