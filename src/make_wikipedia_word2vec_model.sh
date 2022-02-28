echo "[`date '+%Y-%m-%d %H:%M:%S'`] Process start."


# Neologd のインストール"
echo "[`date '+%Y-%m-%d %H:%M:%S'`] Install Neologd..."
git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
./mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -y -n -a
DIC_DIR="`mecab-config --dicdir`/mecab-ipadic-neologd"

# Download Wikipedia data
echo "[`date '+%Y-%m-%d %H:%M:%S'`] Download Wikipedia data..."
mkdir -p ./data
curl https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2 -o data/jawiki-latest-pages-articles.xml.bz2

# テキストファイルに変換
echo "[`date '+%Y-%m-%d %H:%M:%S'`] Clean Wikipedia data..."
git clone https://github.com/attardi/wikiextractor.git
python ./wikiextractor/WikiExtractor.py ./data/jawiki-latest-pages-articles.xml.bz2 -q -b 10M -o ./data/jawiki_texts
cat ./data/jawiki_texts/jawiki-latest-pages-articles-*.txt \
  | sed -e 's/<[^>]*>//g' \
  | sed -e 's/ //g' \
  | sed -e '/^$/d' \
  > ./data/jawiki.txt

# 分かち書きの実行
echo "[`date '+%Y-%m-%d %H:%M:%S'`] Separate words by mecab..."
mecab -d $DIC_DIR -Owakati ./data/jawiki.txt -o ./data/jawiki_wakati.txt -b 163840

# モデルの作成
echo "[`date '+%Y-%m-%d %H:%M:%S'`] Make word2vec model by gensim..."
mkdir -p ./models
python ./make_gensim_model.py


echo "[`date '+%Y-%m-%d %H:%M:%S'`] Process finish."
