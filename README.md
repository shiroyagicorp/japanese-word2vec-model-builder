Japanese Word2Vec Model Builder
===============================

A tool for building gensim word2vec model for Japanese.

It uses MeCab for tokenization with mecab-ipadic-NEologd as a dictionary.
Wikipedia is used as a corpus for training word2vec model.

Trained model
-------------

A trained word2vec model is available at:

http://public.shiroyagi.s3.amazonaws.com/latest-ja-word2vec-gensim-model.zip

Parameters used for training this model are `size=50, window=8, min_count=20`.


Requirements
------------

+ cURL
+ MeCab == 0.996
+ Python >= 3.4

Setup
-----

```
git submodule init
git submodule update
python3 -m venv .env
. .env/bin/activate
pip3 install -r requirements.txt
```

Run
---

An example to build a model at the default path. (output/word2vec.gensim.model)

```
. .env/bin/activate
./build --download-neologd --download-wikipedia-dump --build-gensim-model
```

Another example to specify hyper parameters.

```
. .env/bin/activate
./build -o output/another.model --build-gensim-model --size=50 --window=10 --min-count=5
```

How to use the model
--------------------

```
from gensim.models.word2vec import Word2Vec

model_path = 'output/word2vec.gensim.model'
model = Word2Vec.load(model_path)
```
