import pandas as pd
import spacy
from utils import  keywords_exctractor as ke
from spacy.lang.fr.stop_words import STOP_WORDS
from utils import  ent_extractor as ee
import time


print(time.strftime("%H:%M:%S", time.localtime()), end=' : ')
print('processus started')
df = pd.read_csv("../Protocol_V1/queneau_fr.csv")




nlp = spacy.load("fr_core_news_md")  # chargement du modéle dans Spacy
nlp.Defaults.stop_words |= STOP_WORDS

"""
df_test=df[0:10]
df_test = df_test["texte"].apply(ee.extract_entities,nlp=nlp)
df_test.to_csv('data/test.csv', index = False)
print(df_test.head())
"""


df_keywords = df["texte"].apply(ee.extract_entities,nlp=nlp)
df_result = pd.concat([df, df_keywords], axis=1, join='inner')
print(df_result.head())
df_result.to_csv('data/text_protocol_queneau_fr.csv', index = False)
print(time.strftime("%H:%M:%S", time.localtime()), end=' : ')
print('processus finished')

