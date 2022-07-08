Ce Repositorie à pour but d’analyser la capacité d’abstraction scémantique de différentes méthodes d’extractions de mots clés.  Cette analyse passe le calcul de la similarité cosinus des représentations vectorielle des exercices de Quenau en fonction mots clés généré par les méthodes tester. Les méthodes testées se base sur deux modèles d’exctrations de données  Topical Rank au travers de la PKE  et Teeft au travers de l’API mis à dispositions par le CNRS. Chacun des jeux de données est décliné sous plusieurs formes , sans entité nommée , sans stop Word , avec des mots lemmatisé depuis le texte d’origines. Le repositorie présent regroupe tous les scripts nécessaires à la production de cette expérience , ils peuvent être découpés en 4 étapes . 

Étapes 1: La Génération des Mots clés  cette étape permet de générer des mots clés à partir des modéles sélectionner. 

    PKE_Generate_keyword_with.py : ce script génère les mots clés à partir du modèle Tropical Page Rang et de la librairie PKE 

    TEEFT_Generate_keyword_with.py : Ce script permet de générer des mots clés pour chaque type textes des expériences de Quenau à partir de l’API de teeft proposer par le CNRS Lien de l’api Teeft: scrihttps://objectif-tdm.inist.fr/2021/12/20/extraction-de-termes-teeft/.



Étapes 2 Déclinaisons des Mots clés : ces partis permet de décliner les mots clés générer sous différentes formes dans le but de tester si une forme plutôt qu’une autre facilite l'abstraction sémantique d’un texte. les mots clés sont décliner  sous les formes suviantes :
	-mots clés sans entité
	-mots clés sans stop word
	-mots clés lématise

    PKE_keyword_Déclinaison.py : ce script se charge de modifier les mots clés générés par pke. 

    TEEFT_keyword_Déclinaison.py: ce script se charge de modifier les mots clés générés par Teeft. 




étapes 3 : Cette partie regroupe plusieurs jupyter notebook permettant de calculer la corrélation des différentes données générer précédemment à savoir les mots clés généré par PKE et ses différentes déclinaisons et de même pour les mots clés généré par teeft.  La corrélation cosinus est calculée en prenant un texte comme “clés” auquel les autres texte sont compa rer.  La comparaison passant par la le calcul de la similarité cosinus des textes en fonction de leur reprsantions vectorielle par les mots clés génerer. 

    PKE_cos_simylarity.ipynb : calcul  la similarité cosinus entre les textes de quenaud à partir des mots clés généré par PKE 

    SIMPLE_cos_simylarity.ipynb: Calcul la similarité cosinus des textes avec l’ensemble des mots présent dans le corpus de texte , cette simple similarité cosinus permet d’avoir un point de repérer auquel se comparer. 

    TEEFT_cos_simylarity.ipynb: calcul  la similarité cosinus entre les textes de Quenau à partir des mots clés généré par TEEFT

    TF_IDF.ipynb: Calcul le score de tft IDf de chacun des textes du corpus 



étapes 4 : Analyse des résultats , Contient un jupyter notebook fessant une analyse des résultats obtenus dans les étapes précédentes. 

    analyse_result.ipynb:  c’est Jupyter un  notebook dans le but de produire une première analyse des résultats.
