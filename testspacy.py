import spacy
from spacy.matcher import PhraseMatcher
from spacy.matcher import DependencyMatcher

def important_pos_tagging(sentence):
    nlp = spacy.load("de_core_news_lg")
    doc = nlp(sentence)
    important_pos_tags = ["NOUN", "VERB", "ADJ", "PROPN"]
    filtered_words = [token.text for token in doc if token.pos_ in important_pos_tags]
    #Checking vom Tagging
    pos_tags = [(token.text, token.pos_, token.head.text) for token in doc]
    print(pos_tags)
    #Labeling der Token
    #named_entites = [(ent.text, ent.label_) for ent in doc.ents]
    #print(named_entites)
    return filtered_words

def get_word_stem_and_lemma(word):
    nlp = spacy.load("de_core_news_lg")
    doc = nlp(word)
    token = doc[0]  # Der Token für das gesuchte Wort (es wird erwartet, dass nur ein Wort übergeben wird)
    stem = token.lemma_  # Grundform (Lemma) des Wortes
    lemma = token.morph.get("STEM")  # Wortstamm des Wortes
    return stem, lemma

def get_common_phrases(text):
    # SPrachmodell
    nlp = spacy.load("de_core_news_lg")
    #Init Phrasematcher
    matcher = PhraseMatcher(nlp.vocab)
    #Phrasenliste, die wir suchen
    phrase_list = ["name","geschäftsführer","svlfg"]
    #Phrasen in Matcher hinzufügen
    patterns = [nlp(phrase) for phrase in phrase_list]
    matcher.add("PHRASES", None, *patterns)
    #Text verarbeiten
    doc = nlp(text)
    #Durchsuche Text nach Phrasen
    matches = matcher(doc)
    #Gib Übereinstimmungen aus
    for match_id, start, end in matches:
        matched_phrase = doc[start:end]
        print("Gefundene Phrase:", matched_phrase.text)

def get_word_dependencies(text):

    # Lade das deutsche Sprachmodell
    nlp = spacy.load("de_core_news_lg")

    # Initialisiere den DependencyMatcher
    matcher = DependencyMatcher(nlp.vocab)

    # Definiere ein Muster für die Abhängigkeit, die du suchen möchtest
    pattern = [
        {
            "RIGHT_ID": "target",  # ID für das zu suchende Token
            "RIGHT_ATTRS": {"lemma": "kündigen"},  # Lemma des zu suchenden Tokens
        },
        {
            "LEFT_ID": "target",  # ID des vorherigen Tokens
            "REL_OP": ">",  # Rechtsnachfolger (direkt oder indirekt) des Ziel-Tokens
            "RIGHT_ID": "subject",  # ID für das Subjekt-Token
            "RIGHT_ATTRS": {"dep": "nsubj"},  # Abhängigkeitstyp "nsubj" für das Subjekt-Token
        },
    ]

    # Füge das Muster zum Matcher hinzu
    matcher.add("K_PATTERN", [pattern])

    # Verarbeite den Text
    doc = nlp(text)

    # Durchsuche den Text nach Übereinstimmungen
    matches = matcher(doc)

    # Gib die gefundenen Übereinstimmungen aus
    for match_id, token_ids in matches:
        target_token = doc[token_ids["target"]]
        subject_token = doc[token_ids["subject"]]
        print("Ziel-Token:", target_token.text)
        print("Subjekt-Token:", subject_token.text)


word = "heißt"
stem, lemma = get_word_stem_and_lemma(word)
print(f"Word: {word}")
print(f"Lemma: {lemma}")
print(f"Stem: {stem}")


sentence = "wie ist der name des geschäftsführers der svlfg?"
filtered_words = important_pos_tagging(sentence)
print(filtered_words)#name, geschäftsführer, svlfg

sentence2 = "wie heißt der  geschäftsführer der svlfg?"
filtered_words2 = important_pos_tagging(sentence2)
print(filtered_words2)#heißt, geschäftsführers, svlfg

sentence3 = "wie kann ich meine Mitgliedschaft bei der svlfg kündigen?"
filtered_words3 = important_pos_tagging(sentence3)
print(filtered_words3)#mitgliedschaft, svlfg, kündigen



get_common_phrases("heißt geschäftsführers svlfg")

get_word_dependencies("Wie kann ")