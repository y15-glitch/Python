
# git　コマンド


- ディレクトリ(フォルダー)作成

>mkdir "ディレクトリ名"

---

- ディレクトリの中にファイルを作成する

>touch "ファイル名"

---

- ファイル一覧

>ls
​
root@DESKTOP-99S7J9L:~/skill-UP# ls
consolidate

>ls -a 
 全てのファイル、ディレクトリが表示される

---

- ディレクトリの移動

>cd "パス" (Change Directoryの略)

>cd .. [1つ前のディレクトリに戻る]

oot@DESKTOP-99S7J9L:~/skill-UP# ls
consolidate
root@DESKTOP-99S7J9L:~/skill-UP# cd ..
root@DESKTOP-99S7J9L:~# ls
skill-UP

---

- Gitの中に新しいブランチを作成する

>git switch -c "ブランチ名"

---

+ ブランチの切り替え

>git checkout "ブランチ名"


---

* ステータス確認

>git status

--月--日--時--分に誰がどんな変更を行ったか確認できる

>**赤字は保存されてないよ**
>**青字は保存できてるよ！**

---

- リモートリポジトリから最新の変更を取得

>git pull

---

- ブランチ(枝)
```
git branch
```
main
*test　「＊」がついている箇所が現在のブランチ名

---

- ディレクトリーを保存

> git add "パス名"
 
---

- コミットの仕方

>git commit -m "詳細"

**詳細になにをしたか明確に記載すること**

※別パターン
>git commit -am "詳細"
 am = add + -m　が合わさったもの

---

- コミット内容をアップロード
```
git push 
```
---

- ログ
```
git log
```

## GitHub、Gitについて

- GitHub
 >Gitのソフトウェア開発をサポートするWEBサービス

- Git
 >開発をサポートするソフトウェア
  変更履歴を追えたりなど有能！
