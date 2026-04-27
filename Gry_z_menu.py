import random
import time
import os
os.system('cls')  # Windows
# Black Jack


def blackjack():
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

        def czekaj():
            liczba = 0.3
            time.sleep(liczba)

        print('Zagrajmy w Black Jack')
        czekaj()
        Start_gry = input(
            f'\nChcesz zagarć (tak) czy poznać zasady gry? (zasady) > ').strip().lower()

        if Start_gry in ('nie', 'menu'):
            time.sleep(.3)
            print(f'\nWracam do menu...')
            return

        while Start_gry not in ('tak', 'zasady', 'start', 'nie', 'menu'):
            time.sleep(.3)
            Start_gry = input('''
            Użyj poprawnej komendy.
            Start gry (START).
            Zasady gry (ZASADY).
            Wyjście do Menu (MENU)
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
            Start_gry = input(
                f'\nWiesz jak grać (tak) czy chcesz poznać zasady gry? (zasady) > ').strip().lower()

        while True:
            if Start_gry in ('tak', 'start'):
                time.sleep(.3)
                print(f'\nŚwietnie')
                liczba_graczy = input(f'\nPodaj liczbę graczy (1) czy (2) > ')

            while liczba_graczy not in ('1', '2', 'menu'):
                    time.sleep(.3)
                    liczba_graczy = input(
                        f'\nPodaj liczbę graczy (1) czy (2) > ')
            if liczba_graczy == 'menu':
                        time.sleep(.3)
                        print(f'\nWracam do menu...')
                        return
            elif liczba_graczy in ('1'):
                time.sleep(.3)
                karty_gracz = [random.randint(2, 11), random.randint(2, 11)]
                karty_bot = [random.randint(2, 11), random.randint(2, 11)]

                karty_gracz = popraw_asy(karty_gracz)

                suma_gracz = sum(karty_gracz)
                suma_bot = sum(karty_bot)

                print(
                    f"\nTwoje karty: {', '.join(map(str, karty_gracz))} | wynik > {suma_gracz}")
                print(f'\nKarta bota: {karty_bot[0]}, #')

                if suma_gracz == 21:
                    time.sleep(.3)
                    print(f'\nWygrałeś')
                    time.sleep(.3)
                    wybor = input(
                        f'\nChcesz zagrać jeszcze raz? (tak/nie) > ').strip().lower()
                    while wybor not in ('tak', 'nie'):
                        wybor = input(
                            f'\nChcesz zagrać jeszcze raz? (tak/nie) > ').strip().lower()
                    if wybor != 'tak':
                        break
                    else:
                        continue
                elif suma_gracz < 21:
                    pozycja = input(f'\nHit or Stand > ').strip().lower()
                    while pozycja not in ('hit', 'stand'):
                        time.sleep(.3)
                        pozycja = input(
                            f'\nWybierz co chcesz zrobić. Hit or Stand > ')

                while suma_gracz < 21:
                        if pozycja == 'hit':
                            time.sleep(.3)
                            nowa_karta = random.randint(2, 11)

                            karty_gracz.append(nowa_karta)

                            karty_gracz = popraw_asy(karty_gracz)

                            suma_gracz = sum(karty_gracz)
                            print(f'\nDobierasz kartę')
                            print(
                                f"\nTwoje karty: {', '.join(map(str, karty_gracz))} | wynik > {suma_gracz}")
                            if suma_gracz == 21:
                                time.sleep(.3)
                                print(f'\nWygrałeś!')
                                break
                            elif suma_gracz > 21:
                                time.sleep(.3)
                                print(f'\nPrzegrałeś, wynik: {suma_gracz}')
                                break
                            pozycja = input(
                                f'\nHit or Stand > ').strip().lower()
                            while pozycja not in ('hit', 'stand'):
                                time.sleep(.3)
                                pozycja = input(
                                    f'\nHit or Stand > ').strip().lower()
                        else:
                            break

                if suma_gracz >= 21:
                    return
                time.sleep(.3)
                print(
                    f"\nBot odkrywa karty:{', '.join(map(str, karty_bot))} | wynik > {suma_bot}")
                time.sleep(.3)

                while suma_gracz > suma_bot < 21 or suma_gracz == suma_bot <= 10:
                    time.sleep(.3)
                    karty_bot.append(random.randint(2, 11))
                    karty_bot = popraw_asy(karty_bot)
                    suma_bot = sum(karty_bot)
                    time.sleep(.3)
                    print(f'\nBot dobiera kartę ')
                    time.sleep(.3)
                    print(
                        f"\nKarty Bota:{', '.join(map(str, karty_bot))} | wynik > {suma_bot}")
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

                wybor = input(
                    f'\nChcesz zagrać jeszcze raz? (tak/nie) > ').strip().lower()
                while wybor not in ('tak', 'nie', 'menu'):
                    wybor = input(
                        f'\nChcesz zagrać jeszcze raz? (tak/nie) > ').strip().lower()
                if wybor != 'tak':
                    time.sleep(.3)
                    print(f'\nDzięki za grę!')
                    break
                elif wybor == 'menu':
                        time.sleep(.3)
                        print(f'\nWracam do menu...')
                        return

            elif liczba_graczy in ('2'):
                time.sleep(.3)
                karty_gracz1 = [random.randint(2, 11), random.randint(2, 11)]
                karty_gracz2 = [random.randint(2, 11), random.randint(2, 11)]

                karty_gracz1 = popraw_asy(karty_gracz1)
                karty_gracz2 = popraw_asy(karty_gracz2)

                suma_gracz1 = sum(karty_gracz1)
                suma_gracz2 = sum(karty_gracz2)

                print(
                    f"\nKarty gracza nr.1 : {', '.join(map(str, karty_gracz1))} | wynik > {suma_gracz1}")
                print(
                    f"\nKarty gracza nr.2 : {', '.join(map(str, karty_gracz2))} | wynik > {suma_gracz2}")

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

                pozycja_gracz1 = input(
                    f'\nGracz nr.1 Hit or Stand > ').strip().lower()
                while pozycja_gracz1 not in ('hit', 'stand'):
                    time.sleep(.3)
                    pozycja_gracz1 = input(
                        f'\nWybierz co chcesz zrobić. Hit or Stand > ')

                while suma_gracz1 < 21:
                        if pozycja_gracz1 == 'hit':
                            time.sleep(.3)
                            nowa_karta1 = random.randint(2, 11)
                            karty_gracz1.append(nowa_karta1)
                            karty_gracz1 = popraw_asy(karty_gracz1)
                            suma_gracz1 = sum(karty_gracz1)
                            print(f'\nDobierasz kartę')
                            print(
                                f"\nKarty gracza nr.1 : {', '.join(map(str, karty_gracz1))} | wynik > {suma_gracz1}")
                            print(
                                f"\nKarty gracza nr.2 : {', '.join(map(str, karty_gracz2))} | wynik > {suma_gracz2}")
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
                                return
                            pozycja_gracz1 = input(
                                f'\nHit or Stand > ').strip().lower()
                            while pozycja_gracz1 not in ('hit', 'stand'):
                                time.sleep(.3)
                                pozycja_gracz1 = input(
                                    f'\nHit or Stand > ').strip().lower()
                        else:
                            break

                pozycja_gracz2 = input(
                    f'\nGracz nr. 2 Hit or Stand > ').strip().lower()
                while pozycja_gracz2 not in ('hit', 'stand'):
                    time.sleep(.3)
                    pozycja_gracz2 = input(
                        f'\nWybierz co chcesz zrobić. Hit or Stand > ')

                while suma_gracz2 < 21:
                        if pozycja_gracz2 == 'hit':
                            time.sleep(.3)
                            nowa_karta2 = random.randint(2, 11)

                            karty_gracz2.append(nowa_karta2)

                            karty_gracz2 = popraw_asy(karty_gracz2)

                            suma_gracz2 = sum(karty_gracz2)
                            print(f'\nDobierasz kartę')
                            print(
                                f"\nKarty gracza nr.2: {', '.join(map(str, karty_gracz2))} | wynik > {suma_gracz2}")
                            print(
                                f"\nKarty gracza nr.1 : {', '.join(map(str, karty_gracz1))} | wynik > {suma_gracz1}")
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
                                return
                            pozycja_gracz2 = input(
                                f'\nHit or Stand > ').strip().lower()
                            while pozycja_gracz2 not in ('hit', 'stand'):
                                time.sleep(.3)
                                pozycja_gracz2 = input(
                                    f'\nHit or Stand > ').strip().lower()
                        else:
                            break

                if pozycja_gracz1 == 'stand' and pozycja_gracz2 == 'stand':
                    if suma_gracz1 > suma_gracz2:
                            time.sleep(.3)
                            print(f'''
        \nGracz nr. 1 > {suma_gracz1}
        \nGracz nr. 2 > {suma_gracz2}
        \nWygrywa gracz nr.1''')
                    elif suma_gracz1 < suma_gracz2:
                        time.sleep(.3)
                        print(f'''
        \nGracz nr. 1 > {suma_gracz1}
        \nGracz nr. 2 > {suma_gracz2}
        \nWygrywa gracz nr.2''')
                    elif suma_gracz1 == suma_gracz2:
                        time.sleep(.3)
                        print(f'''
        \nGracz nr. 1 > {suma_gracz1}
        \nGracz nr. 2 > {suma_gracz2}
        \nRemis''')
                    else:
                        break
                wybor = input(
                    f'\nChcesz zagrać jeszcze raz? (tak/nie) > ').strip().lower()
                while wybor not in ('tak', 'nie', 'menu'):
                    wybor = input(
                        f'\nChcesz zagrać jeszcze raz? (tak/nie) > ').strip().lower()
                if wybor != 'tak':
                    time.sleep(.3)
                    print(f'\nDzięki za grę!')
                    break
                elif wybor == 'menu':
                    time.sleep(.3)
                    print(f'\nWracam do menu...')
                    return


# Guess the number
def Zgadnij_liczbe():
            import os
            os.system('cls')  # Windows
            import random
            import time

            def czekaj():
                liczba = 0.3
                time.sleep(liczba)

            czekaj()
            print('''
                    Zagrajmy w "Guess the number"''')
            czekaj()

            while True:
                czekaj()
                start_gry = input('''
                    Wiesz jak grać (tak) czy chcesz poznać zasady gry? (zasady) 
                    > ''').strip().lower()
                while start_gry not in ('tak', 'zasady', 'start', 'menu'):
                    czekaj()
                    start_gry = input('''
                    Użyj poprawnej komendy.
                    (tak / start / menu / zasady)
                    > ''')
                    

                if start_gry == 'zasady':
                    czekaj()
                    print('''
                    Możesz rozegrać od 1 do 1000000 rund
                        
                    Celem gry jest odgadnięcie liczby w różnych przedziałach:
                    Łatwy 0-25
                    Średni 0-100
                    Trudny 0-1000
                    Custom (dowolny przedział)

                    Dostępne są 3 poziomy trudności.
                    Łatwy z nieograniczoną liczbą prób.
                    Średni z 20 próbami
                    Trudny z 10 próbami
                    Custom (dowolna ilość prób)
                    ''')
                    continue

                if start_gry == 'menu':
                    time.sleep(.3)
                    print(f'\nWracam do menu...')
                    return


                if start_gry in ('tak', 'start'):
                    czekaj()
                    print('''
                    Świetnie :)''')
                    break

            while True:    
                czekaj()
                liczby = input('''
                    
                    Wybierz przedział liczb:
                    1. Łatwy 0-25
                    2. Średni 0-100
                    3. Trudny 0-1000
                    4. Custom
                    >  ''').strip().lower()
                
                if liczby in ('1', 'łatwy'):
                    min_liczba, max_liczba = 0, 25
                    break
                elif liczby in ('2', 'średni'):
                    min_liczba, max_liczba = 0, 100
                    break
                elif liczby in ('3', 'trudny'):
                    min_liczba, max_liczba = 0, 1000
                    break
                elif liczby in ('4', 'custom'):
                    while True:
                        try:
                            czekaj()
                            liczba_od = int(input('''
                    Od > '''))
                            if 0 <= liczba_od <= 999999:
                                break
                            else:
                                czekaj()
                                print('''
                    Podaj liczbę z zakresu 0-999999''')
                        except ValueError:
                            czekaj()
                            print('''
                    Podaj liczbę''')

                    while True:
                        try:
                            czekaj()
                            liczba_do = int(input('''
                    Do > '''))
                            if liczba_od < liczba_do <= 1000000:
                                break
                            else:
                                czekaj()
                                print(f'''
                    Liczba musi być większa niż {liczba_od} i mniejsza niż 1000001''')
                        except ValueError:
                            czekaj()
                            print('''
                    Podaj liczbę''')
                    min_liczba = liczba_od
                    max_liczba = liczba_do
                    break



            while True:
                czekaj()
                poziom = input('''
                    Wybierz poziom trudności:
                    1. Łatwy Nieograniczona ilośc zgadnięć
                    2. Średni 20
                    3. Trudny 10
                    4. Custom (dowolna ilość zgadnięć)
                    >  ''').strip().lower()

                if poziom in ('1', 'łatwy'):
                    trudność = 1000000000
                    break
                elif poziom in ('2', 'średni'):
                    trudność = 20
                    break
                elif poziom in ('3', 'trudny'):
                    trudność = 10
                    break
                elif poziom in ('4', 'custom'):
                
                    while True:
                        try:
                            czekaj()
                            trudność = int(input('''
                    Ilość szans > '''))
                            if 1 <= trudność <= 1000000:
                                break
                            else:
                                czekaj()
                                print('''
                    Podaj liczbę z zakresu 1-1000000''')
                        except ValueError:
                            czekaj()
                            print('''
                    Podaj liczbę''')
                    break              
            runda = 1

            while True:
                    czekaj()
                    print(f'''
                    --- Runda {runda} ---''')
                    runda += 1
                    liczba = random.randint(min_liczba, max_liczba)
                    zgadnięcia = 0
                    szansa = trudność
                    while zgadnięcia < trudność:
                            try:
                                czekaj()
                                zgadywana_liczba = int(input('''
                    Liczba > '''))
                            except ValueError:
                                czekaj()
                                print('''
                    Podaj liczbę''')
                                continue


                            zgadnięcia += 1
                            szansa -= 1
                            if szansa > 1000000:
                                tekst_szans = "Pozostałych szans ∞"
                            elif szansa > 20:
                                tekst_szans = "Pozostałych szans > 20"
                            else:
                                tekst_szans = f"Pozostałych szans {szansa}"

                            if zgadywana_liczba < liczba:
                                czekaj()       
                                print(f'''
                    Odgadywana liczba jest większa: {zgadywana_liczba} < #
                    {tekst_szans}''')
                                
                            elif zgadywana_liczba > liczba:
                                czekaj()
                                print(f'''
                    Odgadywana liczba jest mniejsza: {zgadywana_liczba} > #
                    {tekst_szans}''')
                                
                            else:
                                czekaj()
                                print(f'''
                    Gratulacje wygrałeś
                                    
                    Liczba zgadnięć > {zgadnięcia} ''')
                                
                                nastepna_runda = input('''
                    Kolejna runda (tak)
                    Menu (menu)
                    > ''')
                                if nastepna_runda == 'tak':    
                                    break 
                                elif nastepna_runda == 'menu':
                                    return
                                else:
                                    nastepna_runda = input('''
                    Enter = następna runda...''')

                    else:
                                czekaj()
                                print(f'''
                    Niestety przegrałeś
                                    
                    Zgadywana liczba to {liczba}''')
                                nastepna_runda = input('''
                    Kolejna runda (tak)
                    Menu (menu)
                    > ''')
                                if nastepna_runda == 'tak':    
                                    break 
                                elif nastepna_runda == 'menu':
                                    return
                                else:
                                    nastepna_runda = input('''
                    Enter = następna runda...''')


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
            animacja_kropek(random.randint(3,5))
            Zgadnij_liczbe()
        elif wybor in ('2', 'Black Jack'):
            czekaj()
            print(f'\nUruchamiam grę Black Jack')
            print()
            animacja_kropek(random.randint(3,5))
            blackjack()
        elif wybor in ('0', 'wyjście'):
            czekaj()
            print(f"\nKończę program")
            animacja_kropek(random.randint(1,3))
            print()
            quit()
        else:
            czekaj()
            print(f"\nNiepoprawny wybór")



