import pke
from nltk.corpus import stopwords
import spacy
import fr_core_news_md
from spacy.lang.fr.stop_words import STOP_WORDS
import pandas as pd
import requests




def extract_key_words(text ,extractor): #Déclartion d'une fonction permettant de dextraire les entitér en fonction d'un text
    try:
        extractor.load_document(input=text, language='fr', normalization="stemming")
        extractor.candidate_selection()
        extractor.candidate_weighting()
        keyphrases = extractor.get_n_best(n=10)
        list_keyword =list()
        for key_word in keyphrases:
            list_keyword.append(key_word[0])
        return "$".join(list_keyword)

    except Exception as e:
        return (e)


def extract_entities(text): #Déclartion d'une fonction permettant de dextraire les entitér en fonction d'un text
    nlp = spacy.load("fr_core_news_md") # chargement du modéle dans Spacy
    nlp.Defaults.stop_words |= STOP_WORDS
    doc = nlp(text)
    token = [token.text.lower() for token in doc if token.ent_type_ and not token.is_stop]
    return(list(token))


def extract_key_words_clean(text, nlp, extractor):
    # Extractions des entités du texte avec spacy
    print("exctractions des entités")
    doc = nlp(text)
    #lemmatization
    token = [token.text for token in doc if
             token.ent_type_ and not token.is_stop]  # si c'est uune entité autant conserver la CASSE...
    # "aller à Paris" est différent de "faire des paris" !
    #nom adverbe adjectif
    ents = list(token)

    print("entités extraite: " + str(ents))

    # Extractions des mots clés du texte avec pke

    # calcul du nombre de mots clés devant être générer  par pke dans un abstract en fonction de la taille
    n_keywords = round(len(text.split(' ')) * 0.04)
    if n_keywords > 10:
        n_keywords = 10
    print("nombre de mots clés: " + str(n_keywords))

    print("exctractions des mots clés")

    # pos = {'NOUN', 'PROPN', 'ADJ','VERB','ADP','PUNCT','PRON'}
    try:
        extractor.load_document(input=text,
                                language='fr')  # , normalization="stemming") sauf à ce que tu aies testé que çà marche mieux ?
        extractor.candidate_selection()
        extractor.candidate_weighting()
        keyphrases = extractor.get_n_best(n=5)

        list_keyword = list()
        for key_word in keyphrases:
            list_keyword.append(key_word[0])
        keywords = list_keyword

        # Soustractions des entité nommer au mots clés génerer avec pke
        clean_keyword = list()
        for keyword in keywords:
            for ent in ents:
                # ent = ent.lower()
                keyword = str(keyword).replace(str(ent), '')
            clean_keyword.append(keyword)

        deduplicated_clean_keyword = list(set(clean_keyword))
        if ' ' in deduplicated_clean_keyword:
            deduplicated_clean_keyword.remove(' ')
        if '' in deduplicated_clean_keyword:
            deduplicated_clean_keyword.remove('')
    except :
        print("error")
        return None

    print(deduplicated_clean_keyword)
    print("\r")

    return "$".join(deduplicated_clean_keyword)


# pke(text)- entspacy(text)
#text 1 = normal
#text 2 = lematizer
#text 3  = no { 'PROPN','VERB','ADP','PUNCT','PRON'}
#pke(spacy(text))

def protocole_extract_with_Pke(text,nlp,extractor):
    list_of_text = list()
    list_of_text.append(text)
    doc = nlp(text)
    tokens = [tok for tok in doc]


    #Calcul du textes brut sans EN
    print('############################ Start text traitement ###############################')
    print("exctractions des entités")
    token = [token.text for token in doc if token.ent_type_ and not token.is_stop]
    ents = list(token)
    print("entités extraite: " + str(ents))
    print("soustractions des entité au texte")
    ents_text =text
    for ent in ents:
        ents_text= ents_text.replace(ent,'')
    list_of_text.append(ents_text)
    print("fin de soustraction d'entité ")
    print("\r")


    #Calcul du texte avec uniquement noms, adv, adj, verbes
    print("Calcul du texte avec uniquement noms, adv, adj, verbes")
    list_of_token = list()
    for token in tokens:
        if token.pos_ in ("VERB", "ADJ", "ADV", "PROPN"):
            list_of_token.append((token))

    list_of_token = [str(i) for i in list_of_token]
    text_tampon =""
    for token in list_of_token:
        text_tampon = text_tampon+token+" "
    list_of_text.append(text_tampon)
    print("fin Calcul du texte avec uniquement noms, adv, adj, verbes ")
    print("\r")

    """text_tampon=""
    for word in text.replace('.',' ').replace(',',' ').split(' '):
        if word in list_of_token:
            text_tampon=text_tampon+word+" "
    print(text_tampon)"""

    #calcul du texte avec uniquement noms, adv, adj, verbes Lemmatisés
    print("Calcul du texte avec uniquement noms, adv, adj, verbes Lemmatisés")
    list_of_token = list()
    for token in tokens:
        if token.pos_ in ( "ADJ", "ADV", "PROPN"):
            list_of_token.append((token))

        if token.pos_ in ("VERB"):
            list_of_token.append((token.lemma_))

    list_of_token = [str(i) for i in list_of_token]
    text_tampon = ""
    for token in list_of_token:
        text_tampon = text_tampon + token + " "
    list_of_text.append(text_tampon)
    print("fin Calcul du texte avec uniquement noms, adv, adj, verbes Lemmatisés ")
    print("\r")

    #Exctractions des mots clés avec PKE pour chaque élement caluler précedament et stocker dans list_of_text
    list_of_keyword=list()
    for text_test in  list_of_text :
        try:
            keyword_list=extract_key_words(text_test, extractor)
            list_of_keyword.append(keyword_list)
        except Exception as e:
            keyword_list="error: "+str(e)
            list_of_keyword.append(keyword_list)
        print(text_test)
        print(keyword_list)
        print('\r')


    print('############################ End text traitement ###############################')
    print('\r')
    print('\r')
    print('\r')

    list_keywords_text=list_of_keyword[0]
    list_keywords_without_ent=list_of_keyword[1]
    list_keywords_only_VERB_ADJ_ADV_PROPN=list_of_keyword[2]
    list_keywords_only_VERBLemma_ADJ_ADV_PROPN=list_of_keyword[3]


    return pd.Series({'keywords_text': list_of_keyword[0], 'keywords_without_ent': list_of_keyword[1],'keywords_only_VERB_ADJ_ADV_PROPN': list_of_keyword[2],'keywords_only_VERBLemma_ADJ_ADV_PROPN': list_of_keyword[3]})

def keyword_from_teeft(docs):

    # Cette fonction prend en entrer une liste de document pour chaque document avec un résumé en français ou un résumer en anglais
    # la fonction interroge l'api de teeft , l'api renvois une liste de mots clés décrivant le document en fonction de langue du résumer (français ou anglais )
    # Le résultat de la requête est stocké dans le champ teeft_keywords_fr  pour les mots clés français et teeft_keywords_en pour les mots clés anglais
    # Source de l'api : https://openapi.services.inist.fr/?urls.primaryName=Extraction%20de%20termes
    # utils : Outil de conversion de requête curl en divers langages python , c ,java: https: // curlconverter.com /

    headers = {
        'accept': 'application/json',
        # Already added when you pass json= but not when you pass data=
        # 'Content-Type': 'application/json',
    }

    # initialisations des variables pour stocker les requetes  json
    json_data_fr=list()
    for index , doc in docs.iterrows():

        json_data_fr.append({
        'id': index,
        'value':doc["texte"]
        })
        response = requests.post('https://terms-extraction.services.inist.fr/v1/teeft/fr', headers=headers,
                             json=json_data_fr)
        data_fr = response.json()

        # Pour chaque document ayant un résumer en français anglais

    for value in data_fr:
        #docs.loc([int(value["id"])]["teeft_keywords"]= value["value"]
        docs.loc[int(value["id"]), "texte_keyword"] ="$".join(value["value"])
    return(docs)
