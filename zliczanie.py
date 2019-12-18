#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    liczba = 1
    liczby7 = []
    liczby5 = []
    while liczba != 0:
        liczba = int(input('Podaj liczbę: '))
        if liczba == 0:
            print('Ilość liczb podzielnych przez 5: ', len(liczby5))
            print('Ilość liczb podzielnych przez 7: ', len(liczby7))
        elif liczba % 7 == 0:
            liczby7.append(liczba)
            if liczba % 5 == 0:
                liczby5.append(liczba)
        elif liczba % 5 == 0:
            liczby5.append(liczba)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
