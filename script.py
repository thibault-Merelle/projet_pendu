#!/usr/bin/env python3
import logging
import random

#récupération d'une liste de mots dans un fichier exterieur.
def get_word_files(x): #ok retourne la liste de mots
    words = []
    with open(file_names, 'r') as f:
        for line in f:
            words.append(line.strip(" \n"))      
    return x 


#fonct° choix du mot dans la liste:
def fchoix(x:list, y:str):
    y = random.choice(x, k=1)
    return y


#fonction print(_ _ _ _ _ _ _)
def fword(y:str,i:int,x:str):
    i = 0
    base_word = '_'*len(y)
    for x in y:
        i+=1

    if i=0:
        print(base_word)
    else:
        print(incr_word)    

