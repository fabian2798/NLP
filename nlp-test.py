import nltk
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('averaged_perceptron_tagger')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag

def extract_keywords(question):
    # Tokenisierung
    tokens = word_tokenize(question.lower())

    # Entfernen von Stoppwörtern (häufige Wörter ohne viel Bedeutung)
    stop_words = set(stopwords.words('german'))  # Du kannst hier auch die Sprache ändern
    keywords = [token for token in tokens if token not in stop_words]
    print(keywords)

    # POS-Tagging, um nur Nomen, Verben und Adjektive zu behalten
    pos_tags = pos_tag(keywords)

    #Pos-Tagging
    for token, tag in pos_tags:
        print(f"{token}: {tag}")
    #allowed_tags = ['NN', 'NNS', 'VB', 'VBD', 'VBG', 'VBN', 'JJ', 'JJR', 'JJS']
    allowed_tags = ['NN', 'NNS', 'VB', 'VBD', 'VBG', 'VBN']
    keywords = [token for token, tag in pos_tags if tag in allowed_tags]

    return keywords

question = "wie ist der name des geschäftsführers der svlfg?"
keywords = extract_keywords(question)
print(keywords)
