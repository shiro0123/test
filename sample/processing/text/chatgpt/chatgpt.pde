// ライブラリからhttp.requestsをインストールする必要あり
// 日本語がうまく処理されない
import http.requests.*;
import java.nio.charset.StandardCharsets;

Thread asyncThread;
String API_KEY;
String text;

void setup() {
  API_KEY = System.getenv("OPENAI_API_KEY");
  
  
  // 非同期タスクを実行するスレッドを作成
  asyncThread = new Thread(new Runnable() {
    public void run() {
      fetchGPT();
    }
  });
  
  // スレッドを開始
  asyncThread.start();
  
  size(800, 512);
  fill(0);
  textSize(16);
  PFont font = createFont("Meiryo", 50);
  textFont(font);
  text = "Loading...";
}

void draw() {
  background(255);
  text(text, 10, height / 2); // 表示するテキスト, x座標, y座標
}

void fetchGPT() {
  String url = "https://api.openai.com/v1/chat/completions";
  JSONArray messages = new JSONArray();
  // 最初のメッセージオブジェクトを作成
  JSONObject message1 = new JSONObject();
  message1.setString("role", "system");
  message1.setString("content", "answer in english.");
  messages.append(message1);
  
  // 二つ目のメッセージオブジェクトを作成
  JSONObject message2 = new JSONObject();
  message2.setString("role", "user");
  message2.setString("content", "Hello! Please tell me about the history of Japan.");
  messages.append(message2);
  
  // リクエストボディを作成
  JSONObject requestBody = new JSONObject();
  requestBody.setString("model", "gpt-4o");
  requestBody.setJSONArray("messages", messages);
  requestBody.setInt("max_tokens", 150);
  requestBody.setFloat("temperature", 0.5);
  String requestBodyString = requestBody.toString();
  
  // HTTPリクエストを送信
  PostRequest request = new PostRequest(url);
  request.addHeader("Authorization", "Bearer " + API_KEY);
  request.addHeader("Content-Type", "application/json");
  request.addData(requestBodyString);
  request.send();
  
  // レスポンスを取得
  String responseString = request.getContent();
  byte[] bytes = responseString.getBytes(StandardCharsets.ISO_8859_1);
  responseString = new String(bytes, StandardCharsets.UTF_8);
  
  println(responseString);
  
  JSONObject response = parseJSONObject(responseString);
  
  // choices[0].message.contentを取得
  JSONArray choices = response.getJSONArray("choices");
  JSONObject firstChoice = choices.getJSONObject(0);
  String content = firstChoice.getJSONObject("message").getString("content");
  
  text = content;
}