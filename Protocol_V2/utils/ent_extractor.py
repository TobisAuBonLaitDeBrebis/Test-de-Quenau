

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
        text_without_ent = text_without_ent.replace(mot, '')

    text_without_stop_word = [token.text for token in doc if( token.pos_ or token.is_punct or token.is_space )and not token.is_stop]


    texte_verbe_Adj_ADV_PROPN_NOUN = [token.text for token in doc if (token.pos_ in ("VERB", "ADJ", "ADV", "PROPN", "NOUN") or token.is_punct or token.is_space)]
    texteLem_verbe_Adj_ADV_PROPN_NOUN = [token.lemma_ for token in doc if (token.pos_ in ("VERB", "ADJ", "ADV", "PROPN", "NOUN") or token.is_punct or token.is_space)]

    return pd.Series({'texte_sans_entites': "".join(text_without_ent), "text_without_stop_word": " " .join(text_without_stop_word),'texte_verbe_Adj_ADV_PROPN_NOUN': " ".join(texte_verbe_Adj_ADV_PROPN_NOUN),'texteLem_verbe_Adj_ADV_PROPN_NOUN': " ".join(texteLem_verbe_Adj_ADV_PROPN_NOUN)})


"""
texte --> extrait mots clés # test des extracteurs sur différentes styles de texte
texte sans entité--> extrait mots clés # test des extracteurs sur différentes styles de texte
#texte sans mots vides --> extrait mots clés # test sur l'utilité des mots vides
texte --> extrait mots clés --> lemmes # pertinence de la lemmatisation pour l'extraction (par ex. 
texte1 donne (aimera, fleurs, animal)
texte2 donne (aime, fleur, animaux)
"""

