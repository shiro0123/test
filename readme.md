# ShibaLab 合宿 2024 - AI を使おう講座

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
