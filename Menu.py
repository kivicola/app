import os
os.system('cls')  # Windows

import Zgadnij_liczbe
import blackjack
import time

def czekaj():
        liczba = 0.1
        time.sleep(liczba)

def czekaj2():
        liczba = 0.6
        time.sleep(liczba)

def animacja_kropek(ile):
    for _ in range(ile):
        time.sleep(0.4)
        print('.', end='', flush=True)
        time.sleep(0.4)
    print()


while True:
    czekaj()
    print("=== MENU ===")
    czekaj()
    print(f"\n1. Guess The Numebr")
    czekaj()
    print(f"\n2. Black Jack")
    czekaj()
    print(f"\n0. Wyjście")
    czekaj()
    wybor = input(f"\n> ").strip().lower()

    if wybor in ('1', 'Guess The Numebr'):
        czekaj()
        print(f'\nUruchamiam grę Guess the number')
        print()
        animacja_kropek(5)
        Zgadnij_liczbe.Zgadnij_liczbe()
    elif wybor in ('2', 'Black Jack'):
        czekaj()
        print(f'\nUruchamiam grę Black Jack')
        print()
        animacja_kropek(5)
        blackjack.blackjack()
    elif wybor in ('0', 'wyjście'):
        czekaj()
        print(f"\nKończę program")
        animacja_kropek(3)
        print()
        quit()
    else:
        czekaj()
        print(f"\nNiepoprawny wybór")

