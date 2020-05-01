import os
import time
import sys
from Hangman import main
from wordsindo import world_dic


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                ====================
                ===   --------   ===
                ===   |      |   ===
                ===   |      O   ===
                ===   |     \\|/  ===
                ===   |      |   ===
                ===   |     / \\  ===
                ===   -          ===
                ====================
                """,
                # head, torso, both arms, and one leg
                """
                 ===================
                 ===  --------   ===
                 ===  |      |   ===
                 ===  |      O   ===
                 ===  |     \\|/  ===
                 ===  |      |   ===
                 ===  |     /    ===
                 ===  -          ===
                 ===================
                """,
                # head, torso, and both arms
                """
                ====================
                ===   --------   ===
                ===   |      |   ===
                ===   |      O   ===
                ===   |     \\|/  ===
                ===   |      |   ===
                ===   |          ===
                ===   -          ===
                ====================
                """,
                # head, torso, and one arm
                """
                ====================
                ===   --------   ===
                ===   |      |   ===
                ===   |      O   ===
                ===   |     \\|   ===
                ===   |      |   ===
                ===   |          ===
                ===   -          ===
                ====================
                """,
                # head and torso
                """
                ====================
                ===   --------   ===
                ===   |      |   ===
                ===   |      O   ===
                ===   |      |   ===
                ===   |      |   ===
                ===   |          ===
                ===   -          ===
                ====================
                """,
                # head
                """
                ====================
                ===   --------   ===
                ===   |      |   ===
                ===   |      O   ===
                ===   |          ===
                ===   |          ===
                ===   |          ===
                ===   -          ===
                ====================
                """,
                # initial empty state
                """
                ====================
                ===   --------   ===
                ===   |      |   ===
                ===   |          ===
                ===   |          ===
                ===   |          ===
                ===   |          ===
                ===   -          ===
                ====================
                """
    ]
    return stages[tries]


def tittle_scrn():
    os.system('cls')
    print("####################################")
    print("#######  HANGMAN INDONESIA   #######")
    print("####################################")
    print("               - Play -             ")
    print("               - Help -             ")
    print("               - Quit -             ")
    print("####################################")
    print("####################################")
    print("###  Created by : Faizar Rahman  ###")
    print("###    Python Excercise 2020     ###")
    print("####################################")
    tittle_screen_selection()


def help_menu():
    os.system('cls')
    print("####################################")
    print("#######  HANGMAN INDONESIA   #######")
    print("####################################")
    print("     Tebak kata yang akan muncul    ")
    print(" ketikkan 'huruf' atau 'kalimat' nya")
    print("& kalian hanya memilki 5x kesempatan")
    print("####################################")
    print("####################################")
    print("###  Created by : Faizar Rahman  ###")
    print("###     Python Excercise 2020    ###")
    print("####################################")
    tittle_screen_selection()


def tittle_screen_selection():
    option = input("pilihan >").lower()
    if option == ("play"):
        main()
    elif option == ("help"):
        help_menu()
    elif option == ("quit"):
        print("oke,, sampai ketemu lagi!! ")
        time.sleep(0.8)
        sys.exit()


def status_scrn(tries, word):
    print("===========================")
    print(f'sisa nyawa anda = {tries} ')
    print(f'panjang huruf ' + str(len(word)))
    print("===========================")
