#!/usr/bin/env python3
import logging
import random


#def du log :
logging.basicConfig(level=logging.DEBUG,
                    filename="LOG.log",
                    filemode="a", #append ou W pour écraser
                    format='%(asctime)s : %(levelname)s : %(message)s') #manque start et end 

logging.debug("la fonction a bien été éxécutée")
logging.info("info générale")
logging.warning("attention !")
logging.error("une erreur est arrivée")
logging.critical("Erreur critique")






#récupération d'une liste de mots dans un fichier exterieur.
def get_words_files(x):
    words = []
    with open(x, 'r') as f:
        for line in f:
            words.append(line.strip(" \n"))      
    return [words] #sortie = liste de mots


#fonct° choix du mot dans la liste:
def fchoix(x:list):
    z = random.choice(x, k=1)
    z=z.lower() #tout en minuscules
    y=list(z)
    return y #sortie = 1 mot random dans liste y


#fonction print du (_ _ _ _ _ _ _)
def fword(y:list,i:int,x:str):
    out = False #si false = perte d'une vie

    if i==0:
        dict = {}
        word = []
        word = '_'*len(y) #_____

    if i==0 or x not in y:
        return(word) #mot vide si début du jeu ou copie n-1
    else:
        count=0 
        for count,x in enumerate(y)
        #for count in range(0,len(y)+1):
            if x==y[count]:
                word[count] = x 
                out=True  #si true passage réussie

        word = " ".join(word)   #_ _ _ _ _    
        dict[word]=out #sotie = {"word":"bool"}
        return dict
        
#fonction des entrées et test
def finput(y):
    dict={}
    out=False

    while (x.isalpha()==False and len(str(x))!=1) or str(x)!="".join(y):
        x = input("Entrer une lettre ou le mot entier si vous l'avez trouvé :")
        x = x.lower()

        if str(x)!="".join(y):
            out=True #si true = mot trouvé
            
        dict[x]=out 
        return dict #sortie = {"input":"bool"}

#fonction ASCII art pendu
def fimage(x:dict,i:int,life:list): #seul value = false nous interesse pour compteur de vie
    z=x.values()
    if z = False:
        life[i]=x.keys()
        life[0]= life[0].upper()
        life[2]= life[2].upper()

        print("{}{}{}{}{}{}{}{}{}".format(life[2], life[2],life[2],life[2],life[2],life[2],life[2],life[2],life[2],)) 
        print('{}{}      {}'.format(life[1], life[1], life[3]))
        print('{}{}      {}'.format(life[1], life[1], life[3]))
        print('{}{}      {}'.format(life[1], life[1], life[3]))
        print('{}{}      {}'.format(life[1], life[1], life[0]))
        print('{}{}    {} {} {}'.format(life[1], life[1], life[5], life[2], life[5]))
        print('{}{}      {}'.format(life[1], life[1], life[2]))
        print('{}{}     {} {}'.format(life[1], life[1], life[5], life[5]))
        print('{}{}'.format(life[1], life[1]))
        print("{}{}{}{}{}{}{}{}{}{}{}{}{}".format(life[0],life[0],life[0],life[0],life[0], life[0],life[0],life[0],life[0],life[0],life[0],life[0],life[0],)) 

    return life

print("JEU DU PENDU :")
get_words_files()









        """
        switcher = {
            1: 
                print('')
                print('')
                print('')
                print('')
                print('')
                print('')
                print('')
                print('')
                print(' __________')
                print('[XXXXXXXXXX]')
            2:
                print('||')
                print('||')
                print('||')
                print('||')
                print('||')
                print('||')
                print('||')
                print('||')
                print('| \________')
                print('[XXXXXXXXXX]')
            3:
                print('____________')
                print('|/')
                print('||')
                print('||')
                print('||')
                print('||')
                print('||')
                print('||')
                print('| \________')
                print('[XXXXXXXXXX]')
            4:
                print('__________X__')
                print('|/        |')
                print('||        |')
                print('||        |')
                print('||')
                print('||')
                print('||')
                print('||')
                print('| \________')
                print('[XXXXXXXXXX]')         
            5:
                print('__________X__')
                print('|/        |')
                print('||        |')
                print('||        |')
                print('||       _O_')
                print('||        |')
                print('||')
                print('||')
                print('| \________')
                print('[XXXXXXXXXX]') 
            6:
                print('__________X__')
                print('|/       /')
                print('|/       |')
                print('||       /')
                print('||     _O')
                print('||      |\')
                print('||     /|')
                print('||')
                print('| \________')
                print('[XXXXXXXXXX]')                                    
        }
        return switcher.get(i)

    else:
        break   
"""


