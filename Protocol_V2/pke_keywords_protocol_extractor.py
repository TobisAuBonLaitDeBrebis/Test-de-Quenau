#Objectif retourner des liste de mots clés particuliére
import pandas as pd
import spacy
from spacy.lang.fr.stop_words import STOP_WORDS
import time


def words_in_string(word_list, a_string):
    # cette function retourne les mot contenue à la fois dans word_list et a_string
    return list(set(word_list).intersection(a_string))


print(time.strftime("%H:%M:%S", time.localtime()), end=' : ')
print('processus started')
df = pd.read_csv("data/Keyword_with_PKE_queneau_fr.csv") # récupération des données de base de l'épérience





nlp = spacy.load("fr_core_news_md")  # chargement du modéle dans Spacy
nlp.Defaults.stop_words |= STOP_WORDS
# Mots clés de base
#df=df[0:10] pour les test

#df.reindex(columns = df.columns.tolist()  + ['keyword_without_ent','keyword_without_stop_word'])
dict={}
for index ,row in df.iterrows():
    doc = nlp(row["texte"])
    list_keywords = list()
    for keyword in str(row["texte_keyword"]).split('$'):
        for word in keyword.split(" "):
            list_keywords.append(word)
    print(list_keywords)


    ########################## Mots clés sans entité.##############################
    entites = [token.text for token in doc if token.ent_type_ and not token.is_stop]
    df.loc[index,'keyword_without_ent']="$".join([keyword for keyword in list_keywords if keyword not in entites])
    ###############################################################################

    ########################## Mots clés sans stop words.##########################
    #V1:
    #keyword_without_stop_word= [token.text for token in doc if( token.pos_ or token.is_punct or token.is_space )and not token.is_stop]
    #df.loc[index,"keyword_without_stop_word"] = " ".joinwords_in_string(row["texte_keyword"].split(), keyword_without_stop_word))
    #V2:

    df.loc[index, "keyword_without_stop_word"] = "$".join([keyword for keyword in list_keywords if keyword not in STOP_WORDS])
    ###############################################################################

    ########################## Mots clés lematisé.#################################
    # Creation d'un dictionnaire avec en clés le mots simple et en valuer le Mot lématise
    df.loc[index, "keywords_lematisations"] = "$".join([token.lemma_ for token in doc if token.text in list_keywords])

    ###############################################################################
df.to_csv("data/Keyword_with_PKE_queneau_frprotocol_V2.csv")
print(time.strftime("%H:%M:%S", time.localtime()), end=' : ')
print('processus end')