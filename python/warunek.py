#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    a = int(input ('Podaj liczbę: '))
    b = int(input ('Podaj liczbę: '))
    if b > b:
        print ('A jest większe od B')
    elif b > a:
        print ('B jest większe od A')
    else:
        print ('Liczbe są równe')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
