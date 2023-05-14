print("Hello")

# git　コマンド

- ディレクトリ(フォルダー)作成

```　Python
mkdir "ディレクトリー名"(ファイル名)
```
---

- ディレクトリーした中にファイルを作成する
```　Python
touch "ファイル名"
```
---

- リスト確認
​```　　Python
ls
​```
---

- ディレクトリの移動

```　　Python
cd "ファイル名" (Change Directoryの略)

cd .. [1つ前のファイルに戻る]
```
---

- GitHubの中に新しいディレクトリを作成する

```　Python
git switch -c "ファイル名"
```
---

- ステータス確認
```　Python
git status
```
###### **赤字**の場合は、保存が出来ていない
###### **青字**保存完了

---

- リモートリポジトリから最新の変更を取得

```　Python
git pull
```
---

- ブランチ
```　Python
git branch
```
##### main
##### *test　「＊」がついている箇所が現在のリポジトリ
---
- ディレクトリーを保存
```　Python
 git add .←現在の場所にあるファイルを保存する
 ```
---
- コミットの仕方
``` Python
git commit -m "詳細"
```
##### 詳細になにをしたか明確に記載すること
---

- コミット内容をアップロード
``` Python
git push 
```
---

- ログ
``` Python
git log
```

