#!/usr/bin/env python
# -*- coding: utf-8 -*-

def przedział_liczbowy():
    min = input('Najmniejsza liczba w przedziale: ')
    max = input('Największa liczba w przedziale: ')
    liczba = min
    liczby = []
    while min <= liczba >= max:
        liczby.append([liczba])
        liczba = liczba + 1 
    print(liczby)
def main(args):
    przedział_liczbowy()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
