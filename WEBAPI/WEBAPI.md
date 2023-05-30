#WEBAPI作成方法

API:
>

Flask：
>PythonのWEBアプリケーションフレームワーク
 軽量、自由度が高い
 フォルダ構造をシンプルで分かりやすいのが特徴

フレームワーク：
>


##環境構築
Flask、Python3をインストール


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

route
http://127.0.0.1:5000/
開いてのreturnの値を出力する

#ファイルネーム
#アプリのインスタンス化
 FLASKをインスタンス化
 フレームワークを作る





export FLSK_APP=hello

FLASK_APP:
ローカル環境変数

「hello」値returnを出力

ローカル環境変数：
PCのどこでも使用できる変数
PC統一の変数

デバックモード:
コードを変更したときに自動で変更を出力してくれること
ON、OFFの違い
OFF変更が反映されない
export FLASK_ENV=development

Debugger is active!
Debug mode: on



@app.route("/japan")
def japan():
    return "Hello Japan"

http://127.0.0.1:5000/ japan

@app.route("/")
URLを作成する感じ


Ctrl+Dで複数選択



@app.route("/japan/tokyo")
def japan():
    return "Hello tokyo"

可変URL

@app.route("/japan/<city>")
def japan(city):
    return f"Hello {city} in japan"



ul　アンフォーダーリストの略