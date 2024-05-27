# ShibaLab 合宿 2024 - AI を使おう講座 SAMPLES

## はじめに - 全体で必要なもの

### direnv のインストール

フォルダごとの環境変数を設定するために direnv のインストールを行ってください。

WSL Ubuntu + bash

```bash
sudo apt install direnv
sudo echo 'eval "$(direnv hook bash)"' >> ~/.bashrc
```

### .envrc の設定

.envrc ファイルを使って、実際にフォルダ固有の環境変数を設定します。
今回は、API キーを設定するために使います。

```bash
cp .envrc.temp .envrc
```

.envrc ファイルを開いて、API キーを設定してください。
キーは当日配布します。

```env
export OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
...
```

その後、direnv を再読み込みしてください。

```bash
direnv allow
```

### mise のインストール

asdf, mise, anyenv などのバージョン管理ツールを使うと、複数のバージョンの Python や Node.js を使い分けることができます。
今回は、特にインストールが簡単な mise を使います。

```bash
curl https://mise.run | sh
echo 'eval "$(~/.local/bin/mise activate bash)"' >> ~/.bashrc
```

### Python、Node.js のインストール

mise を使って、Python と Node.js をインストールします。

```bash
mise i
```

### ライブラリのインストール

Python のライブラリをインストールします。

```bash
pip install -r requirements.txt
```

Node.js のライブラリをインストールします。

```bash
npm install
```

### API 　サンプルの実行

API サンプルは Python, JavaScript, processing の 3 種類を用意しています。
全てのサンプルは`sample`フォルダに格納されています。

サンプルにある LLM は、`ChatGPT`, `Claude`, `Gemini`の 3 種類です。
また、画像生成 AI として `DALL-E`および`Stable Diffusion`のサンプルも格納されています。

このテスト環境では code runner を使うことを推奨します。
この`readme`が存在するフォルダを最上位層として VSCode を開き、Code Runner を使って実行してください。

特別な理由でコマンドで実行する場合は以下のコマンドを実行してください。

python

```bash
python ./path/to/file.py
```

node.js

```bash
node ./path/to/file.js
```

### web app サンプルの実行

HTML/CSS/JavaScript で構成された簡単な Web アプリケーションのサンプルも用意しています。
ソースコードは`app`フォルダ内に格納されています。

サンプルの実行は、この`readme`が存在するフォルダを最上位層として VSCode を開き、以下のコマンドを実行してください。

```bash
npm run start
```

[localhost:4000](http://localhost:4000)にアクセスすると、Web アプリケーションが表示されます。

HTML ファイルや CSS ファイル、JavaScript ファイルを変更した場合は自動でリロードされます。
