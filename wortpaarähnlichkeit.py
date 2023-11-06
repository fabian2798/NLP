import gensim.downloader as api
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Lade das Word2Vec-Modell
word2vec_model = api.load("word2vec-google-news-300")

def compute_pair_embedding(pair):
    # Berechne die Word Embeddings für jedes Wort im Paar
    word_embeddings = [word2vec_model[word] for word in pair]

    # Berechne den Durchschnitt der Word Embeddings, um das Paar zu repräsentieren
    pair_embedding = np.mean(word_embeddings, axis=0)

    return pair_embedding

def compute_pair_similarity(pair1, pair2):
    # Berechne die Embeddings für die Wortpaare
    pair1_embedding = compute_pair_embedding(pair1)
    pair2_embedding = compute_pair_embedding(pair2)

    # Berechne die Cosinus-Ähnlichkeit zwischen den Word Embeddings-Vektoren der Paare
    similarity = cosine_similarity([pair1_embedding], [pair2_embedding])[0][0]

    return similarity

# Beispiel
pair1 = ["heißen", "geschäftsführer", "svlfg"]
pair2 = ["name", "geschäftsführers", "svlfg"]
similarity = compute_pair_similarity(pair1, pair2)
print(f"Ähnlichkeit zwischen Paar 1 und Paar 2: {similarity}")
