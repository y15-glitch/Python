- ファイル一覧

>ls
​
root@DESKTOP-99S7J9L:~/skill-UP# ls
consolidate


 ディレクトリの移動

>cd "パス" (Change Directoryの略)

>cd .. [1つ前のディレクトリに戻る]

oot@DESKTOP-99S7J9L:~/skill-UP# ls
consolidate
root@DESKTOP-99S7J9L:~/skill-UP# cd ..
root@DESKTOP-99S7J9L:~# ls
skill-UP


Q　コミットログを1行づつ表示する
>　git log --oneline

例）
1：b6fdaae (HEAD -> consolidate, origin/consolidate) 保管場所を修正
2：345cb9a (origin/test, test) 練習用で作成した
3：212f153 README.mdファイル追加

1行目から最新…3行目1番古い　順に並べられている
