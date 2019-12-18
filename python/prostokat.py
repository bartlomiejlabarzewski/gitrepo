#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  prostokat.py

def main(args):
    znak = input('Podaj znak: ')
    h = int(input('Wysokość prostokąta: '))
    w = int(input('Szerokość prostokąta: '))
    if h > 20:
        print('Wysokość nie może przekraczać 20 znaków')
    while 20 >= h > 0:
        print(znak)
        h = h - 1
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
