#Objectif retourner des liste de mots clés particuliére
import numpy as np
import pandas as pd
import spacy
import numpy
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

for index ,row in df.iterrows():
    doc = nlp(row["texte"])

    ########################## Mots clés sans entité.##############################
    entites = [token.text for token in doc if token.ent_type_ and not token.is_stop]
    df.loc[index,'keyword_without_ent']=" ".join([keyword for keyword in row["texte_keyword"].split() if keyword not in entites])
    ###############################################################################

    ########################## Mots clés sans stop words.##########################
    #V1:
    #keyword_without_stop_word= [token.text for token in doc if( token.pos_ or token.is_punct or token.is_space )and not token.is_stop]
    #df.loc[index,"keyword_without_stop_word"] = " ".joinwords_in_string(row["texte_keyword"].split(), keyword_without_stop_word))
    #V2:
    df.loc[index, "keyword_without_stop_word"] = " ".join([keyword for keyword in row["texte_keyword"].split() if keyword not in STOP_WORDS])
    ###############################################################################

    ########################## Mots clés lematisé.#################################
    # Creation d'un dictionnaire avec en clés le mots simple et en valuer le Mot lématise
    df.loc[index, "keywords_lematisations"] = " ".join([token.lemma_ for token in doc if token.text in row["texte_keyword"].split()])
    print("\r")
    ###############################################################################

df.to_csv("data/Keyword_with_PKE_queneau_frprotocol_V2.csv")
print(time.strftime("%H:%M:%S", time.localtime()), end=' : ')
print('processus end')

"""
total_keywords_list = list()
for keywords in df[:1]["texte_keyword"]:
    for keyword in keywords.split():
        total_keywords_list.append(keyword)

total_keywords_list=list(set(total_keywords_list))
df_test = pd.DataFrame(index=df["title "], columns=total_keywords_list)

for index , row in df_test.iterrows():
    for keyword in total_keywords_list:
        #df_test.loc[index,keyword] = str(df["texte"][df["title "] == index]).count(keyword)
        df_test.loc[index, keyword] = 1


array_test=df_test.to_numpy()
print(df_test.head())

for key in  df_test.keys():
    print(key)
    print(df_test[key].sum())


matrice_correlation = list()
for index , vector1 in enumerate(array_test):
    vector_corelation = list()
    for vector2 in array_test:
        vector_corelation.append(numpy.dot(vector1, vector2, out=None))

    matrice_correlation.append(vector_corelation)
    print("\r")
test=np.array(matrice_correlation)

for index1,row in enumerate(test):
    for  index2 ,column in enumerate(row):
       #print(column)
        pass

print(test)
"""
