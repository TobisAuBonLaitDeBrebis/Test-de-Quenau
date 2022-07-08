# importations des librairies nécessaires
import pandas as pd
from utils import  keywords_exctractor as ke
import pke
import time
import os
from utils.definitions import ROOT_DIR





print(time.strftime("%H:%M:%S", time.localtime()), end=' : ')
print('processus started')

df = pd.read_csv(os.path.join(ROOT_DIR, 'Data', 'queneau_fr.csv'))#récupérations des données et stockage à l'intérieur d'un datafrme pour être manipulé
print(df.head())

extractor = pke.unsupervised.TopicalPageRank()#Chargement du modéle topical Rank

for key in df.keys():
    if key not in("title"):
        print(key)
        df[key+"_keyword"] = df[key].apply(ke.extract_key_words,extractor=extractor) #ajout d'un champ keyword à partir de la librairie PKE
print(df.head())

df.to_csv(os.path.join(ROOT_DIR, 'Data', 'PKE_Keyword.csv'), index = False)#Enregistrement sous forme de CSV dans le fichier /Data/PKE_keyword.csv
print(time.strftime("%H:%M:%S", time.localtime()), end=' : ')
print('processus finished')
