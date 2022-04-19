

import pandas as pd
from collections import Counter
import plotly.graph_objects as go
import requests
import io
import spacy
from spacy.lang.fr.stop_words import STOP_WORDS

def extract_entities(text,nlp): #Déclaration d'une fonction permettant de d'extraire les entités en fonction d'un texte
    """Retourne la liste des entités nommées identifiées dans le texte,
       le texte comportant les noms, adjectifs, verbes et adverbes et excluant le reste
       le texte Lemmatisé comportant les noms, adjectifs, verbes et adverbes et excluant le reste"""
    doc = nlp(text)
    entites = [token.text for token in doc if token.ent_type_ and not token.is_stop] # En conservant la casse !
    text_without_ent = text
    for mot in entites:
        text_without_ent = text.replace(mot, '')
    texte = [token.text for token in doc if (token.pos_ in ("VERB", "ADJ", "ADV", "PROPN", "NOUN") or token.is_punct or token.is_space) and not token.is_stop]
    texteLem = [token.lemma_ for token in doc if (token.pos_ in ("VERB", "ADJ", "ADV", "PROPN", "NOUN") or token.is_punct or token.is_space) and not token.is_stop]

    return pd.Series({'texte_sans_entites': "".join(text_without_ent), 'texte': " " .join(texte), "texte_lemmatisé": " " .join(texteLem)})
