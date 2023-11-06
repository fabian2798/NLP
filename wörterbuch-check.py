import gensim.downloader as api

# Lade das Word2Vec-Modell
word2vec_model = api.load("word2vec-google-news-300")

# Beispiel: Zugriff auf die Word Embeddings für das Wort "apple"
word = "Geschäftführer"
if word in word2vec_model.key_to_index:
    word_embedding = word2vec_model[word]
    print(f"Word Embedding für '{word}': {word_embedding}")
else:
    print(f"'{word}' ist nicht im Word2Vec-Modell enthalten.")

word = "heist"
if word in word2vec_model.key_to_index:
    word_embedding = word2vec_model[word]
    print(f"Word Embedding für '{word}': {word_embedding}")
else:
    print(f"'{word}' ist nicht im Word2Vec-Modell enthalten.")

word = "svlfg"
if word in word2vec_model.key_to_index:
    word_embedding = word2vec_model[word]
    print(f"Word Embedding für '{word}': {word_embedding}")
else:
    print(f"'{word}' ist nicht im Word2Vec-Modell enthalten.")