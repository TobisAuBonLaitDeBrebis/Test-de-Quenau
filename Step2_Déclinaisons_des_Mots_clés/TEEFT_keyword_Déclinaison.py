#Objectif retourner des liste de mots clés particuliére
import pandas as pd
import spacy
from spacy.lang.fr.stop_words import STOP_WORDS
import time
import os
from utils.definitions import ROOT_DIR

print(time.strftime("%H:%M:%S", time.localtime()), end=' : ')
print('processus started')
df = pd.read_csv(os.path.join(ROOT_DIR, 'Data', 'TEEFT_Keyword.csv'))#récupération des données précedament générer dans l'étape 1
nlp = spacy.load("fr_core_news_md")  # chargement du modéle dans Spacy
nlp.Defaults.stop_words |= STOP_WORDS

dict={}
for index ,row in df.iterrows():
    doc = nlp(row["texte"])

    #####################Convesrions des données en de list#######################
    list_keywords = list()
    for keyword in str(row["texte_keyword"]).split('$'):
        for word in keyword.split(" "):
            list_keywords.append(word)
    print(list_keywords)
    ###############################################################################

    ############### j'enleve les majuscule pour la vectorisations##################
    df.loc[index, 'texte'] = row["texte"].lower()
    ###############################################################################

    ########################## Mots clés sans entité.##############################
    entites = [token.text for token in doc if token.ent_type_ and not token.is_stop]
    df.loc[index,'keyword_without_ent']="$".join([keyword for keyword in list_keywords if keyword not in entites])
    ###############################################################################

    ########################## Mots clés sans stop words.##########################
    df.loc[index, "keyword_without_stop_word"] = "$".join([keyword for keyword in list_keywords if keyword not in STOP_WORDS])
    ###############################################################################

    ########################## Mots clés lematisé.#################################
    df.loc[index, "keywords_lematisations"] = "$".join([token.lemma_ for token in doc if token.text in list_keywords])
    ###############################################################################

df.to_csv(os.path.join(ROOT_DIR, 'Data', 'TEEFT_Keyword_Déclinaison.csv')) #Enregistrement sous forme de CSV dans le fichier /Data/TEEFT_Keyword_Déclinaison.csv
print(time.strftime("%H:%M:%S", time.localtime()), end=' : ')
print('processus end')