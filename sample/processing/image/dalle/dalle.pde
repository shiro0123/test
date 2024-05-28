import http.requests.*;
import java.nio.charset.StandardCharsets;

// ライブラリからhttp.requestsをインストールする必要あり
Thread asyncThread;
String API_KEY;
String imageUrl;
PImage loadedImage;
boolean imageLoaded = false;

void setup() {
  API_KEY = System.getenv("OPENAI_API_KEY");
  // 非同期タスクを実行するスレッドを作成
  asyncThread = new Thread(new Runnable() {
    public void run() {
      fetchDalle();
    }
  });
  
  // スレッドを開始
  asyncThread.start();
  
  size(800, 512);
  fill(0);
  textSize(16);
  PFont font = createFont("Meiryo", 50);
  textFont(font);
  imageUrl = "Loading...";
}

void draw() {
  background(255);
  if (imageLoaded) {
    // 画像が読み込まれた場合、画像を描画
    image(loadedImage, 0, 0, width, height);
  } else {
    // 画像が読み込まれていない場合、テキストを描画
    text(imageUrl, 10, height / 2);
  }
}

void fetchDalle() {
  String url = "https://api.openai.com/v1/images/generations";
  // リクエストボディを作成
  JSONObject requestBody = new JSONObject();
  requestBody.setString("model", "dall-e-2");
  requestBody.setString("prompt", "a white siamese cat");
  requestBody.setInt("n", 1);
  requestBody.setString("size", "1024x1024");
  String requestBodyString = requestBody.toString();
  
  // HTTPリクエストを送信
  PostRequest request = new PostRequest(url);
  request.addHeader("Authorization", "Bearer " + API_KEY);
  request.addHeader("Content-Type", "application/json");
  request.addData(requestBodyString);
  request.send();
  
  // レスポンスを取得
  String responseString = request.getContent();
  
  println(responseString);
  
  JSONObject response = parseJSONObject(responseString);
  
  // data[0].urlを取得
  JSONArray data = response.getJSONArray("data");
  JSONObject firstData = data.getJSONObject(0);
  imageUrl = firstData.getString("url");
  
  // 画像を読み込む
  loadedImage = loadImage(imageUrl, "png");
  
  // 画像が読み込まれたかチェック
  if (loadedImage != null) {
    imageLoaded = true;
  } else {
    imageUrl = "Failed to load image.";
    println("Failed to load image.");
  }
}