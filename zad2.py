#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sumuj_liczby():
    a = int(input('Podaj 1 liczbę: '))
    b = int(input('Podaj 2 liczbę: '))
    suma = 0
    if a < 0 or b < 0 or a >=  b:
        print('Błędne dane!')
        return
    else:
        for liczba in range (a, b + 1):
            suma = suma + liczba
        print(suma)

def sumuj_parzyste():
    a = b = -1
    while a < 0:
        a = int(input('Podaj 1 liczbę: '))
    while b <= a:
        b = int(input('Podaj 2 liczbę: '))
    suma = 0
    for liczba in range (a, b + 1):
        if liczba % 2 == 0:
            suma = suma + liczba
    print(suma)
    
def sumuj_nieparzyste():
    a = b = -1
    while a < 0:
        a = int(input('Podaj 1 liczbę: '))
    while b <= a:
        b = int(input('Podaj 2 liczbę: '))
    suma = 0
    for liczba in range (a, b + 1):
        if liczba % 2 == 1:
            suma = suma + liczba
    print(suma)

def main(args):
    # sumuj_liczby()
    # sumuj_parzyste()
    sumuj_nieparzyste()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
