#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  oceny.py

def pobierzOceny():
    oceny = []
    ocena = float(input('Podaj ocenę: '))
    while ocena > 0:
        if ocena < 7:
            oceny.append(ocena)
            ocena = float(input('Podaj ocenę: '))
        else:
            print('Błędna ocena!')
            ocena = float(input('Podaj ocenę: '))
    return oceny
def liczSrednia(oceny):
    print(sum(oceny) / len(oceny))

def main(args):
    oceny = pobierzOceny()
    liczSrednia(oceny)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
