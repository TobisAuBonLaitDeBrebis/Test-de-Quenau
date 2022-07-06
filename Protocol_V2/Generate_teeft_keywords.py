from utils import  keywords_exctractor as ke
import pandas as pd
import time
print(time.strftime("%H:%M:%S", time.localtime()), end=' : ')
print('processus started')

df = pd.read_csv("queneau_fr.csv")
df=ke.keyword_from_teeft(df)
df.to_csv("data/Keyword_from_teeft.csv")
print(time.strftime("%H:%M:%S", time.localtime()), end=' : ')

