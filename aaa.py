#Black Jack
import os
os.system('cls')  # Windows
 
import random
import time
def popraw_asy(karty):
    suma = sum(karty)
    while suma > 21 and 11 in karty:
        indeks = karty.index(11)
        karty[indeks] = 1
        suma = sum(karty)
    return karty

print('Zagrajmy w Black Jack')
time.sleep(.2)
Start_gry = input('Wiesz jak grać (tak) czy chcesz poznać zasady gry? (zasady) > ').strip().lower()

if Start_gry in ('nie', 'quit'):
    time.sleep(.2)
    print('Do zobaczenia :)')
    quit()


while Start_gry not in ('tak', 'zasady', 'start', 'nie', 'quit'):
    time.sleep(.2)
    Start_gry = input('''
    Użyj poprawnej komendy.
    Start gry (START).
    Zasady gry (ZASADY).
    Wyjście z gry (QUIT)
    > ''').strip().lower()


if Start_gry == 'zasady':
    time.sleep(.2)
    print('''
          Celem gry jest zdobycie 21 punktów,
          lub posiadnie większej ilości punktów niż
          przeciwnik.
          '1' punkt możesz zmienić na '11' punktów
          i odwrotnie.
          Gra kończy się natychmiast kiedy, któryś z graczy zdobędzie
          21 punktów (wygrana) lub więcen niż 21 punktów (przegrana).
          'Hit' oznacza dobranie karty, 'Stand' oznacz pas do końca rundy.
         
    ''')
    Start_gry = input('Wiesz jak grać (tak) czy chcesz poznać zasady gry? (zasady) > ').strip().lower()


if Start_gry in ('tak', 'start'):
    time.sleep(.2)
    print('Świetnie')
    liczba_graczy = input('Podaj liczbę graczy (1) czy (2) > ')

    while liczba_graczy not in ('1', '2'):
        time.sleep(.2)
        liczba_graczy = input('Podaj liczbę graczy (1) czy (2) > ')
   


if liczba_graczy in ('1'):
    time.sleep(.2)
    karty_gracz = [random.randint(2, 11), random.randint(2, 11)]
    karty_bot = [random.randint(2, 11), random.randint(2, 11)]
    
    karty_gracz = popraw_asy(karty_gracz)

    suma_gracz = sum(karty_gracz)
    suma_bot = sum(karty_bot)
    
    print(f"Twoje karty: {', '.join(map(str, karty_gracz))} | wynik > {suma_gracz}")
    print(f'Karta bota: {karty_bot[0]}, #')

    

    if suma_gracz == 21:
        time.sleep(.2)
        print('Wygrałeś')
        quit()


pozycja = input('Hit or Stand > ').strip().lower()
while pozycja not in ('hit', 'stand'):
    time.sleep(.2)
    pozycja = input('Wybierz co chcesz zrobić. Hit or Stand > ')


while suma_gracz < 21:
        if pozycja == 'hit':
            time.sleep(.2)
            nowa_karta = random.randint(2, 11)

            karty_gracz.append(nowa_karta)


            karty_gracz = popraw_asy(karty_gracz)

            suma_gracz = sum(karty_gracz)
            print()
            print('Dobierasz kartę')
            print(f"\nTwoje karty: {', '.join(map(str, karty_gracz))} | wynik > {suma_gracz}")
            if suma_gracz == 21:
                time.sleep(.2)
                print('Wygrałeś!')
                break
            elif suma_gracz > 21:
                time.sleep(.2)
                print(f'Przegrałeś, wynik: {suma_gracz}')
                break
            pozycja = input('Hit or Stand > ').strip().lower()
            while pozycja not in ('hit', 'stand'):
                time.sleep(.2)
                pozycja = input('Hit or Stand > ').strip().lower()
        else:
            break

if suma_gracz >= 21:
    quit()
print(f"\nBot odkrywa karty:{', '.join(map(str, karty_bot))} | wynik > {suma_bot}")

while suma_bot < 17 or suma_gracz > suma_bot < 21:
    time.sleep(.2)
    karty_bot.append(random.randint(2, 11))
    karty_bot = popraw_asy(karty_bot)
    suma_bot = sum(karty_bot)
    print()
    print('Bot dobiera kartę ')
    print(f"\nKarty Bota:{', '.join(map(str, karty_bot))} | wynik > {suma_bot}")

if suma_bot > 21 or suma_gracz > suma_bot:
    time.sleep(.2)
    print("Wygrałeś!")
elif suma_gracz == suma_bot:
    time.sleep(.2)
    print("Remis")
else:
    time.sleep(.2)
    print("Bot wygrał")
    