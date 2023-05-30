#WEBAPI作成

from flask import Flask

app = Flask(__name__)

html="""
<h1>HTML練習</h1>
<ul>
　　<li>箇条書き1</li>
　　<li>箇条書き2</li>
　　<li>箇条書き3</li>
</ul>
"""

@app.route("/")
def hello():
    return html
    