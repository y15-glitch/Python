#WEBAPI作成方法

- API
アプリケーション・プログラム・インターフェース
インターフェース(何かと何かを繋げる)
アプリケーションとプログラムを繋げる
<br>
- Flask
PythonのWEBアプリケーションフレームワーク
軽量、自由度が高い
フォルダ構造をシンプルで分かりやすいのが特徴
<br>
- フレームワーク
テンプレートのようなもの

```python

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello World"

```
[API URL](http://127.0.0.1:5000/)


``` python
from flask import Flask
from flask import render_template

@app.route("/japan/<city>")
def japan(city):
    return f"Hello {city} in japan"

#http://127.0.0.1:5000/japan/<city>cityの
#部分に都市(例Tokyo)を入れると
#「Hello Tokyo in japan」と出力される
```

`export FLASK_APP=ファイル名`
`flask run`

app = Flask(__name__)ファイルネーム
アプリのインスタンス化(WEB、オブジェクトの作成)
 
@app.route("/")
開いてのreturnの値を出力する
URLを作成する
http://127.0.0.1:5000/

デバックモード:
コードを変更したときにリアルタイムで変更を出力してくれること
ON、OFFの違い
OFFだと毎回`flask run`を行わないと変更が反映されない
デバックモードON:
`export FLASK ENV=development`

デバックモードONの状態
`Debugger is active!`
`Debug mode: on`

Ctrl+Dで複数選択