# -*- coding: utf-8 -*-
import datetime
from gensim.models import word2vec

# モデルの作成
data = word2vec.Text8Corpus("./data/jawiki_wakati.txt")
model = word2vec.Word2Vec(data, vector_size=200, window=10, min_count=10, sg=1, negative=10, epochs=10, workers=8, seed=1025)

# モデルの出力
str_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
model.save(f"./models/jawiki_{str_now}.model")
