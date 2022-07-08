#Importations des librairies nécessaires
from utils import  keywords_exctractor as ke
import pandas as pd
import time
import os
from utils.definitions import ROOT_DIR
print(time.strftime("%H:%M:%S", time.localtime()), end=' : ')
print('processus started')


df = pd.read_csv(os.path.join(ROOT_DIR, 'Data', 'queneau_fr.csv'))#récupérations des données et stockage à l'intérieur d'un dataframe pour être manipulé
print(df.head())

df=ke.keyword_from_teeft(df)#ajout d'un champ keyword à partir de la librairie Teeft
df.to_csv(os.path.join(ROOT_DIR, 'Data', 'TEEFT_Keyword.csv'), index = False)#Enregistrement sous forme de CSV dans le fichier /Data/TEEFT_keyword.csv
print(time.strftime("%H:%M:%S", time.localtime()), end=' : ')
print('processus end')

