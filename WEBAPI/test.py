import MeCab

text="私は学校に行きます"
m=MeCab.Tagger("-O wakati")
print(m.parse(text))
