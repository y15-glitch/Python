import MeCab

mecab=MeCab.Tagger("-O wakati")

text="私は学校に行きます"

result=mecab.pardse(text)
print(result)