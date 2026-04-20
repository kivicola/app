#Guess the number
import os
os.system('cls')  # Windows

import random
import time

print('''
        Zagrajmy w "Guess the number"''')
time.sleep(.2)

while True:
    time.sleep(.2)
    start_gry = input('''
        Wiesz jak grać (tak) czy chcesz poznać zasady gry? (zasady) 
        > ''').strip().lower()
    while start_gry not in ('tak', 'zasady', 'start', 'quit'):
        time.sleep(.2)
        start_gry = input('''
        Użyj poprawnej komendy.
        (tak / start / quit / zasady)
        > ''')
        

    if start_gry == 'zasady':
        time.sleep(.2)
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

    if start_gry in 'quit':
        time.sleep(.2)
        print('''
        Do zobaczenia :)
        ''')
        quit()

    if start_gry in ('tak', 'start'):
        time.sleep(.2)
        print('''
        Świetnie :)''')
        break
    

while True:
    try:
        time.sleep(.2)
        rundy = int(input('''
        Ile rund chcesz zagrać? 
        > '''))
        if 0 < rundy <= 1000000:
            break
    except:
        time.sleep(.2)
        print('''
        Podaj liczbe''')


while True:    
    time.sleep(.2)
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
                time.sleep(.2)
                liczba_od = int(input('''
        Od > '''))
                if 0 <= liczba_od <= 999999:
                    break
                else:
                    time.sleep(.2)
                    print('''
        Podaj liczbę z zakresu 0-999999''')
            except ValueError:
                time.sleep(.2)
                print('''
        Podaj liczbę''')

        while True:
            try:
                time.sleep(.2)
                liczba_do = int(input('''
        Do > '''))
                if liczba_od < liczba_do <= 1000000:
                    break
                else:
                    time.sleep(.2)
                    print(f'''
        Liczba musi być większa niż {liczba_od} i mniejsza niż 1000001''')
            except ValueError:
                time.sleep(.2)
                print('''
        Podaj liczbę''')
        min_liczba = liczba_od
        max_liczba = liczba_do
        break



while True:
    time.sleep(.2)
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
                time.sleep(.2)
                trudność = int(input('''
        Ilość szans > '''))
                if 1 <= trudność <= 1000000:
                    break
                else:
                    time.sleep(.2)
                    print('''
        Podaj liczbę z zakresu 1-1000000''')
            except ValueError:
                time.sleep(.2)
                print('''
        Podaj liczbę''')
        break
            
for runda in range(1, rundy + 1):
    time.sleep(.2)
    print(f'''
        --- Runda {runda} ---''')

    liczba = random.randint(min_liczba, max_liczba)
    zgadnięcia = 0
    szansa = trudność

    while zgadnięcia < trudność:
            try:
                time.sleep(.2)
                zgadywana_liczba = int(input('''
        Liczba > '''))
            except ValueError:
                time.sleep(.2)
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
                time.sleep(.2)       
                print(f'''
        Odgadywana liczba jest większa: {zgadywana_liczba} < #
        {tekst_szans}''')
                
            elif zgadywana_liczba > liczba:
                time.sleep(.2)
                print(f'''
        Odgadywana liczba jest mniejsza: {zgadywana_liczba} > #
        {tekst_szans}''')
                
            else:
                time.sleep(.2)
                print(f'''
        Gratulacje wygrałeś
                      
        Liczba zgadnięć > {zgadnięcia} ''')
                input('''
        Enter = następna runda...''')
                break 
    else:
                time.sleep(.2)
                print(f'''
        Niestety przegrałeś
                      
        Zgadywana liczba to {liczba}''')
                input('''
        Enter = następna runda...''')
    print('''
        Koniec gry
        ''')       
