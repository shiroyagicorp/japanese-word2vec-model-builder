import multiprocessing

from gensim.models.word2vec import Word2Vec


def build_gensim_w2v_model(model_path, iter_tokens, size, window, min_count):
    """
    Parameters
    ----------
    model_path : string
        Path of Word2Vec model
    iter_tokens : iterator
        Iterator of documents, which are lists of words
    """
    model = Word2Vec(
        size=size,
        window=window,
        min_count=min_count,
        workers=multiprocessing.cpu_count()
    )
    model.build_vocab(iter_tokens())
    model.train(iter_tokens())
    model.init_sims(replace=True)
    model.save(model_path)
