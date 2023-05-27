
# Git

## GitHub、Gitについて

- GitHub
 >Gitのソフトウェア開発をサポートするWEBサービス

- Git
 >開発をサポートするソフトウェア
  変更履歴を追えたりなど有能！

---

##Git　コマンド


###ディレクトリ、ファイル関係

- ディレクトリ(フォルダー)作成

>mkdir "ディレクトリ名"

mkdir = make directory

---

- ディレクトリの中にファイルを作成する

>touch "ファイル名"

---

- ファイル一覧

>ls
​
>ls -a 
 全てのファイル、ディレクトリが表示される

---

- ディレクトリの移動

>cd "パス" (Change Directoryの略)

>cd .. [1つ前のディレクトリに戻る]

 cd = change directory

---

###branch関係

- ブランチ(枝)

branch = 枝、別々の時間軸
分岐(枝分かれ)させる事で別々のバージョンを開発・管理できる。

git branch

main
*test　「＊」がついている箇所が現在のブランチ名

---

- Gitで新しいブランチを作成する

>git switch -c "ブランチ名"
 -c = create

---

+ ブランチの切り替え

>git checkout "ブランチ名"

>git switch "ブランチ名"

---

* ステータス確認

>git status

--月--日--時--分に誰がどんな変更を行ったか確認できる

>**赤字は保存されてないよ**
>**青字は保存できてるよ！**

---

- リモートリポジトリから最新の変更を取得

>git pull

リモートのmainブランチからpullする場合
git pull origin main

pull = 引っ張る
リモートリポジトリから持ってくるてきな

---

- gitのステージングに指定したディレクトリ・ファイルに追加する

> git add "パス名"

add = 追加

---

###コミット

- コミットの仕方

>git commit -m "詳細"

**詳細になにをしたか明確に記載すること**

※別パターン
>git commit -am "詳細"
 am = add + -m　が合わさったもの

---

- コミット内容をアップロード

>git push 

---

###履歴を確認する

- ログ

>git log