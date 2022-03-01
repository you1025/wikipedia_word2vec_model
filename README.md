# 環境構築(Docker じゃない版)

## Amazon Linux2

```sh
# 開発ツールの導入
$ sudo yum -y update
$ sudo yum groupinstall -y "Development Tools"

# タイムゾーンを JST に変更
$ sudo ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
```

### mecab のインストール

mecab 本体

```sh
$ wget 'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE' -O mecab-0.996.tar.gz
$ tar xzf mecab-0.996.tar.gz
$ cd mecab-0.996
$ ./configure
$ make
$ make check
$ sudo make install
$ cd ..
```

### python 環境の構築

```sh
$ pip3 install wikiextractor gensim
```

# モデルの構築

aws の c5.2xlarge(8 cpu / 16 GB-Mem) でだいたい 5 時間くらい掛かる。

```sh
$ git clone https://github.com/you1025/wikipedia_word2vec_model.git
$ cd wikipedia_word2vec_model/src
$ nohup sh make_wikipedia_word2vec_model.sh &
```
