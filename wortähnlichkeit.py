import gensim.downloader as api
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Lade das Word2Vec-Modell
word2vec_model = api.load("word2vec-google-news-300")

def compute_word_similarity(word1, word2):
    # Berechne die Word Embeddings für die Wörter
    embedding_word1 = word2vec_model[word1]
    embedding_word2 = word2vec_model[word2]

    # Berechne die Cosinus-Ähnlichkeit zwischen den Word Embeddings-Vektoren
    similarity = cosine_similarity([embedding_word1], [embedding_word2])[0][0]

    return similarity

# Beispiel
word1 = "heißt"
word2 = "name"
similarity = compute_word_similarity(word1, word2)
print(f"Ähnlichkeit zwischen '{word1}' und '{word2}': {similarity}")
