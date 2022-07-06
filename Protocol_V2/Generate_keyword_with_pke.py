import pandas as pd
import spacy
from utils import  keywords_exctractor as ke
from spacy.lang.fr.stop_words import STOP_WORDS
import pke
import time




print(time.strftime("%H:%M:%S", time.localtime()), end=' : ')
print('processus started')

df = pd.read_csv("queneau_fr.csv")
print(df.head())

extractor = pke.unsupervised.TopicalPageRank()

for key in df.keys():
    if key not in("title"):
        print(key)
        df[key+"_keyword"] = df[key].apply(ke.extract_key_words,extractor=extractor)

print(df.head())
df.to_csv('data/Keyword_with_PKE_queneau_fr.csv', index = False)
print(time.strftime("%H:%M:%S", time.localtime()), end=' : ')
print('processus finished')