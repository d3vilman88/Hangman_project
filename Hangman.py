import random 
from words import word_list
from Display import display_hangman, status_scrn
import sys 
import os 
import time


def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letter = []
    guessed_words = []
    tries = 6

    time.sleep(0.5)
    os.system("cls")
    print(word)
    print("ayo main hangman!!!")
    print(display_hangman(tries))
    print (word_completion)
    print("\n")
    print(tries)
    while not guessed and tries >0:
        guess = input("ayo coba tebak kata atau hurufnya,,, ").upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letter:
                print("udah pernah di coba,, coba yang lain" + guess)
            elif guess not in word:
                print (guess + "ga ada dalam kata itu")
                tries -=1 
                guessed_letter.append(guess)
            else : 
                print ("keren..." + guess + "adalah hufur nya")
                guessed_letter.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices :
                    word_as_list[index] = guess 
                word_completion= "".join(word_as_list)
                if "_" not in word_completion :
                    guessed = True



        elif len(guess)==len(word) or len(guess) != len(word) and guess.isalpha():
            if guess.upper() == word.upper():
                print("keeern" + guess + "adalah kata yang benar")
                guessed = True 
                word_completion = word  
            elif guess not in guessed_words:
                print("kata itu salah")
                tries -=1 
                guessed_words.append(guess)
            elif guess in guessed_words:
                print ("kata itu udah di coba")
                print(guessed_words)
                             

        elif guess is not str:
            print ("nit a valid guess...")


        time.sleep(0.5)
        os.system("cls")
        print("ayo main hangman!!!")
        print(display_hangman(tries))
        print (word_completion)
        print("\n")
        status_scrn()
    if  guessed:
        print("selamat!!!")
    else :
        print("orang nya kegantung,, anda gagal!!, kata yang benar adalah " + word + "coba lagi taun depan!!")

def main() : 
    word = get_word()
    print(word)
    play(word)
    while input("mau main lagi? (Y/N)" ).upper() == "Y":
        word = get_word()
        play(word)

def status_scrn(): 
    print("====================")
    print(f"=== nyawa" + str(tries))
    print("====================")

if __name__ == "__main__" :
    main()