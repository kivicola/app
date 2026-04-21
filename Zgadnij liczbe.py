#Guess the number
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
if __name__ == "__main__":
    Zgadnij_liczbe()
