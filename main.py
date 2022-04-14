import pandas as pd
import spacy
from utils import  keywords_exctractor as ke
from spacy.lang.fr.stop_words import STOP_WORDS
import pke
import time

"""
Protocole :
pour chaque texte de Queneau :
0. Générer avec spacy :
    a. texte brut,
    B. texte sans EN
    c. texte avec uniquement noms, adv, adj, verbes
    c. texte avec uniquement noms, adv, adj, verbes Lemmatisés
2. extracteur Mots clés (Pke) ?
3. comparaison des résultats (niveau lexical ?....)
4. résultats (et on triche pas, on n'adapte pas : on mesure ce que l'on peut et point barre.)
"""


"""
# Test sur un seul texte 
test =Dans l'S, à une heure d'affluence. Un type dans les vingt-six ans, chapeau mou avec cordon remplaçant
le ruban, cou trop long comme si on lui avait tiré dessus. Les gens descendent. Le type en question s'irrite
contre un voisin. Il lui reproche de le bousculer chaque fois qu'il passe quelqu'un. Ton pleurnichard qui se
veut méchant. Comme il voit une place libre, se précipite dessus. précipite '''

nlp = spacy.load("fr_core_news_md")  # chargement du modéle dans Spacy
nlp.Defaults.stop_words |= STOP_WORDS
extractor = pke.unsupervised.TopicalPageRank()
test=ke.protocole_extract_with_Pke(test,nlp,extractor)
print(test[4])
print(len(test))
"""

print(time.strftime("%H:%M:%S", time.localtime()), end=' : ')
print('processus started')

#Test sur l'ensemblde des textes
df = pd.read_csv("data/queneau_fr.csv")
nlp = spacy.load("fr_core_news_md")  # chargement du modéle dans Spacy
nlp.Defaults.stop_words |= STOP_WORDS

extractor = pke.unsupervised.TopicalPageRank() #chargement du modéle topicalRank
"""
df_test =df[0:1]
#df_test["keywords_text"], df_test["keywords_without_ent"], df_test["keywords_only_VERB_ADJ_ADV_PROPN"], df_test["keywords_only_VERBLemma_ADJ_ADV_PROPN"]=
func_test= df_test["texte"].apply(ke.protocole_extract_with_Pke,nlp=nlp,extractor=extractor)
result = pd.concat([df_test, func_test], axis=1, join='inner')
print(result.head())
"""
df_keywords = df["texte"].apply(ke.protocole_extract_with_Pke,nlp=nlp,extractor=extractor)
df_result = pd.concat([df, df_keywords], axis=1, join='inner')
df_result.to_csv('data/keyword_queneau_fr.csv', index = False)
print(df_result.head())

print(time.strftime("%H:%M:%S", time.localtime()), end=' : ')
print('processus finished')

