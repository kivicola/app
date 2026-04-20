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
time.sleep(.3)
Start_gry = input(f'\nChcesz zagarć (tak) czy poznać zasady gry? (zasady) > ').strip().lower()

if Start_gry in ('nie', 'quit'):
    time.sleep(.3)
    print(f'\nDo zobaczenia :)')
    quit()


while Start_gry not in ('tak', 'zasady', 'start', 'nie', 'quit'):
    time.sleep(.3)
    Start_gry = input('''
    Użyj poprawnej komendy.
    Start gry (START).
    Zasady gry (ZASADY).
    Wyjście z gry (QUIT)
    > ''').strip().lower()


if Start_gry == 'zasady':
    time.sleep(.3)
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
    Start_gry = input(f'\nWiesz jak grać (tak) czy chcesz poznać zasady gry? (zasady) > ').strip().lower()

while True:
    if Start_gry in ('tak', 'start'):
        time.sleep(.3)
        print(f'\nŚwietnie')
        liczba_graczy = input(f'\nPodaj liczbę graczy (1) czy (2) > ')

        while liczba_graczy not in ('1', '2'):
            time.sleep(.3)
            liczba_graczy = input(f'\nPodaj liczbę graczy (1) czy (2) > ')
    


    if liczba_graczy in ('1'):
        time.sleep(.3)
        karty_gracz = [random.randint(2, 11), random.randint(2, 11)]
        karty_bot = [random.randint(2, 11), random.randint(2, 11)]
        
        karty_gracz = popraw_asy(karty_gracz)

        suma_gracz = sum(karty_gracz)
        suma_bot = sum(karty_bot)
        
        print(f"\nTwoje karty: {', '.join(map(str, karty_gracz))} | wynik > {suma_gracz}")
        print(f'\nKarta bota: {karty_bot[0]}, #')

        

        if suma_gracz == 21:
            time.sleep(.3)
            print(f'\nWygrałeś')
            time.sleep(.3)
            wybor = input(f'\nChcesz zagrać jeszcze raz? (tak/nie) > ').strip().lower()
            while wybor not in ('tak', 'nie'):
                wybor = input(f'\nChcesz zagrać jeszcze raz? (tak/nie) > ').strip().lower()
            if wybor != 'tak':
                break
            else:
                continue
        elif suma_gracz < 21:
            pozycja = input(f'\nHit or Stand > ').strip().lower()
            while pozycja not in ('hit', 'stand'):
                time.sleep(.3)
            pozycja = input(f'\nWybierz co chcesz zrobić. Hit or Stand > ')


        while suma_gracz < 21:
                if pozycja == 'hit':
                    time.sleep(.3)
                    nowa_karta = random.randint(2, 11)

                    karty_gracz.append(nowa_karta)


                    karty_gracz = popraw_asy(karty_gracz)

                    suma_gracz = sum(karty_gracz)
                    print(f'\nDobierasz kartę')
                    print(f"\nTwoje karty: {', '.join(map(str, karty_gracz))} | wynik > {suma_gracz}")
                    if suma_gracz == 21:
                        time.sleep(.3)
                        print(f'\nWygrałeś!')
                        break
                    elif suma_gracz > 21:
                        time.sleep(.3)
                        print(f'\nPrzegrałeś, wynik: {suma_gracz}')
                        break
                    pozycja = input(f'\nHit or Stand > ').strip().lower()
                    while pozycja not in ('hit', 'stand'):
                        time.sleep(.3)
                        pozycja = input(f'\nHit or Stand > ').strip().lower()
                else:
                    break

        if suma_gracz >= 21:
            quit()
        time.sleep(.3)
        print(f"\nBot odkrywa karty:{', '.join(map(str, karty_bot))} | wynik > {suma_bot}")
        time.sleep(.3)

        while suma_gracz > suma_bot < 21 or suma_gracz == suma_bot <= 10 :
            time.sleep(.3)
            karty_bot.append(random.randint(2, 11))
            karty_bot = popraw_asy(karty_bot)
            suma_bot = sum(karty_bot)
            time.sleep(.3)
            print(f'\nBot dobiera kartę ')
            time.sleep(.3)
            print(f"\nKarty Bota:{', '.join(map(str, karty_bot))} | wynik > {suma_bot}")
            time.sleep(.3)

        if suma_bot > 21 or suma_gracz > suma_bot:
            time.sleep(.3)
            print(f"\nWygrałeś!")
        elif suma_gracz == suma_bot:
            time.sleep(.3)
            print(f"\nRemis")
        else:
            time.sleep(.3)
            print(f"\nBot wygrał")


        wybor = input(f'\nChcesz zagrać jeszcze raz? (tak/nie) > ').strip().lower()
        while wybor not in ('tak', 'nie'):
            wybor = input(f'\nChcesz zagrać jeszcze raz? (tak/nie) > ').strip().lower()
        if wybor != 'tak':
            time.sleep(.3)
            print(f'\nDzięki za grę!')
            break
            

    elif liczba_graczy in ('2'):
        time.sleep(.3)
        karty_gracz1 = [random.randint(2, 11), random.randint(2, 11)]
        karty_gracz2 = [random.randint(2, 11), random.randint(2, 11)]
        
        karty_gracz1 = popraw_asy(karty_gracz1)
        karty_gracz2 = popraw_asy(karty_gracz2)

        suma_gracz1 = sum(karty_gracz1)
        suma_gracz2 = sum(karty_gracz2)
        
        print(f"\nKarty gracza nr.1 : {', '.join(map(str, karty_gracz1))} | wynik > {suma_gracz1}")
        print(f"\nKarty gracza nr.2 : {', '.join(map(str, karty_gracz2))} | wynik > {suma_gracz2}")

        if suma_gracz1 == 21 and suma_gracz1 > suma_gracz2:
            time.sleep(.3)
            print(f'\nWygrał gracz numer 1 ')
            break
        elif suma_gracz2 == 21 and suma_gracz2 > suma_gracz1:
            time.sleep(.3)
            print(f'\nWygrał gracz numer 2 ')
            break
        elif suma_gracz1 == suma_gracz2 == 21:
            time.sleep(.3)
            print(f'''\n
    Remis
    Gracz nr.1 {suma_gracz1}
    Gracz nr.2 {suma_gracz2}''')
            break


        pozycja_gracz1 = input(f'\nGracz nr.1 Hit or Stand > ').strip().lower()
        while pozycja_gracz1 not in ('hit', 'stand'):
            time.sleep(.3)
            pozycja_gracz1 = input(f'\nWybierz co chcesz zrobić. Hit or Stand > ')

        while suma_gracz1 < 21:
                if pozycja_gracz1 == 'hit':
                    time.sleep(.3)
                    nowa_karta1 = random.randint(2, 11)
                    karty_gracz1.append(nowa_karta1)
                    karty_gracz1 = popraw_asy(karty_gracz1)
                    suma_gracz1 = sum(karty_gracz1)
                    print(f'\nDobierasz kartę')
                    print(f"\nKarty gracza nr.1 : {', '.join(map(str, karty_gracz1))} | wynik > {suma_gracz1}")
                    print(f"\nKarty gracza nr.2 : {', '.join(map(str, karty_gracz2))} | wynik > {suma_gracz2}")
                    if suma_gracz1 == 21:
                        time.sleep(.3)
                        print(f'''\n
    Wygrywa gracz nr.1 wynik > {suma_gracz1}
    Gracz nr2. wynik > {suma_gracz2}''')
                    elif suma_gracz1 > 21:
                        time.sleep(.3)
                        print(f'''
    Przegrałeś, wynik: {suma_gracz1}
    Wygrywa gracz nr.2 z wynikiem {suma_gracz2}''')
                        quit()
                    pozycja_gracz1 = input(f'\nHit or Stand > ').strip().lower()
                    while pozycja_gracz1 not in ('hit', 'stand'):
                        time.sleep(.3)
                        pozycja_gracz1 = input(f'\nHit or Stand > ').strip().lower()
                else:
                    break


        pozycja_gracz2 = input(f'\nGracz nr. 2 Hit or Stand > ').strip().lower()
        while pozycja_gracz2 not in ('hit', 'stand'):
            time.sleep(.3)
            pozycja_gracz2 = input(f'\nWybierz co chcesz zrobić. Hit or Stand > ')


        while suma_gracz2 < 21:
                if pozycja_gracz2 == 'hit':
                    time.sleep(.3)
                    nowa_karta2 = random.randint(2, 11)

                    karty_gracz2.append(nowa_karta2)


                    karty_gracz2 = popraw_asy(karty_gracz2)

                    suma_gracz2 = sum(karty_gracz2)
                    print(f'\nDobierasz kartę')
                    print(f"\nKarty gracza nr.2: {', '.join(map(str, karty_gracz2))} | wynik > {suma_gracz2}")
                    print(f"\nKarty gracza nr.1 : {', '.join(map(str, karty_gracz1))} | wynik > {suma_gracz1}")
                    if suma_gracz2 == 21:
                        time.sleep(.3)
                        print(f'''\n
    Wygrywa gracz nr.2 wynik > {suma_gracz2}
    \nGracz nr2. wynik > {suma_gracz1}''')
                        break
                    elif suma_gracz2 > 21:
                        time.sleep(.3)
                        print(f'''
    Przegrałeś, wynik: {suma_gracz2}
    \nWygrywa gracz nr.1 z wynikiem: {suma_gracz1}''')
                        quit()
                    pozycja_gracz2 = input(f'\nHit or Stand > ').strip().lower()
                    while pozycja_gracz2 not in ('hit', 'stand'):
                        time.sleep(.3)
                        pozycja_gracz2 = input(f'\nHit or Stand > ').strip().lower()
                else:
                    break

        if pozycja_gracz1 == 'stand' and pozycja_gracz2 == 'stand':     
            if suma_gracz1 > suma_gracz2:
                    time.sleep(.3)
                    print(f'''\n
Gracz nr. 1 > {suma_gracz1}  
\nGracz nr. 2 > {suma_gracz2}
\nWygrywa gracz nr.1''')
            elif suma_gracz1 < suma_gracz2:
                time.sleep(.3)
                print(f'''\n
Gracz nr. 1 > {suma_gracz1}  
\nGracz nr. 2 > {suma_gracz2}
\nWygrywa gracz nr.2''')
            elif suma_gracz1 == suma_gracz2:
                time.sleep(.3)
                print(f'''\n
Gracz nr. 1 > {suma_gracz1}       
\nGracz nr. 2 > {suma_gracz2}
\nRemis''')
            else:
                break
        wybor = input(f'\nChcesz zagrać jeszcze raz? (tak/nie) > ').strip().lower()
        while wybor not in ('tak', 'nie'):
            wybor = input(f'\nChcesz zagrać jeszcze raz? (tak/nie) > ').strip().lower()
        if wybor != 'tak':
            time.sleep(.3)
            print(f'\nDzięki za grę!')
            break
