# -*- coding: utf-8 -*-
import datetime
from gensim.models import word2vec
from gensim.models.callbacks import CallbackAny2Vec

class callback(CallbackAny2Vec):
    def __init__(self):
        self.epoch = 0
        self.cumulative_loss_to_prev_epoch = 0

    def on_epoch_end(self, model):
        self.epoch += 1

        cumulative_loss = model.get_latest_training_loss()
        loss_on_latest_epoch = cumulative_loss - self.cumulative_loss_to_prev_epoch

        print(f"epoch: {self.epoch:2d} - loss: {loss_on_latest_epoch:13.5f}")

        self.cumulative_loss_to_prev_epoch = cumulative_loss


# モデルの作成
data = word2vec.Text8Corpus("./data/jawiki_wakati.txt")
model = word2vec.Word2Vec(data, vector_size=100, window=5, min_count=10, workers=4, sg=1, negative=5, compute_loss=True, callbacks=[callback()], epochs=5, seed=1025)

# モデルの出力
str_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
model.save(f"./models/jawiki_{str_now}.model")
