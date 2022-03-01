# -*- coding: utf-8 -*-
import datetime
from gensim.models import word2vec
from gensim.models.callbacks import CallbackAny2Vec

class PrintLoss(CallbackAny2Vec):
    """
    epoch 毎に Loss を算出して表示
    """
    def __init__(self):
        self.epoch = 0
        self.cumulative_loss_to_prev_epoch = 0

    def on_epoch_end(self, model):
        self.epoch += 1

        # Loss の算出
        # model.get_latest_training_loss だと累積が出力されるらしいので通算 Loss を保持しておいて当該 epoch の値を算出 
        cumulative_loss = model.get_latest_training_loss()
        loss_on_latest_epoch = cumulative_loss - self.cumulative_loss_to_prev_epoch

        print(f"epoch: {self.epoch:2d} - loss: {loss_on_latest_epoch:13.5f}")

        self.cumulative_loss_to_prev_epoch = cumulative_loss


# モデルの作成
# パラメータ一覧: https://radimrehurek.com/gensim/models/word2vec.html#gensim.models.word2vec.Word2Vec
data = word2vec.Text8Corpus("./data/jawiki_wakati.txt")
model = word2vec.Word2Vec(data, vector_size=200, window=10, min_count=5, workers=8, sg=1, negative=10, compute_loss=True, callbacks=(PrintLoss()), epochs=5, seed=1025)

# モデルの出力
str_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
model.save(f"./models/jawiki_{str_now}.model")
