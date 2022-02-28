# 環境構築(Docker じゃない版)

## Amazon Linux2

```sh
# 開発ツールの導入
$ sudo yum update
$ sudo yum groupinstall -y "Development Tools"

# JST
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

Neologd

```sh
$ git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
$ ./mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -a -y
```

辞書の場所を確認

```
$ echo "`mecab-config --dicdir`/mecab-ipadic-neologd"
```

### python 環境の構築

```sh
$ pip install wikiextractor gensim
```

# モデルの構築

```sh
$ cd src
$ sh make_wikipedia_word2vec_model.sh
```
