import logging
import random
from hanging_boy import lives_live



logging.basicConfig(level=logging.DEBUG,
                    filename="LOG_hangman.log",
                    filemode="a",
                    format='%(asctime)s : %(levelname)s : %(message)s')

logging.debug("la fonction a bien été éxécutée")
logging.warning("attention !")







#récupération d'une liste de mots dans un fichier exterieur.
def get_words_files():
    try:
        x = 'mots.txt'
        words = []
        with open(x, 'r') as f:
            for line in f:
                words.append(line.strip(" \n"))
        logging.debug("mot.tx read succesfully")
    except:
        logging.warning("no mots.txt file in directory")

    word = random.choice(words)  
    word = word.upper()
    print(word)
    logging.debug("function random choice success")
    return word 


def hangman():
    try:
        word = get_words_files() # lettres du mot
        word_letters = set(word)
        used_letters = set () # lettres utilisées
        life = 7


        while len(word_letters) > 0 and life > 0:
            print('\n you have used this letters : ',' '.join(used_letters))
            print(' you have ', life,' life remaining !')

            my_list = [letter if letter in used_letters else '_' for letter in word]
            print(lives_live[life])
            print('\n Your word : ',' '.join(my_list))

            gamer_letter = input('guess a letter : ').upper()

            if len(gamer_letter) == 1:
                used_letters.add(gamer_letter)
                
                if gamer_letter in word_letters:
                    word_letters.remove(gamer_letter)
                
                else :
                    life = life - 1
                    print(gamer_letter,' not in the word.')

            elif gamer_letter in used_letters:
                print('You have already try this letter ')

            else:
                life = life - 1
                print('wrong letter!')   

    

        if life == 0:
            print('Sorry, you died !')
            print('Your word was : ',word)
            logging.debug("failure, losing ended ")
        else:
            logging.debug("success ended file")
            print('Succes, your word was : ',word)
        
        logging.info("hangman main function succes")
    except:
        logging.warning("hangman main function failed")

    if __name__ == '__main__':
        hangman()

#print(get_words_files(sys.argv[1]))  
#print(hangman(get_words_files(sys.argv[1])))  