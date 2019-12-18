#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle

def kwadrat(bok):
    for i in range(4):
        turtle.forward(bok)
        turtle.left(90)

        
def kwadraty(ile, bok, krok):
    turtle.setup(1280, 720)
    turtle.pencolor("#ff0000")
    turtle.pensize(3)
    for i in range(ile):
        print(i)
        kwadrat(bok + krok * i)

def gwiazda(bok):
    for i in range(5):
        turtle.forward(bok)
        turtle.right(144)
        turtle.forward(bok)
        turtle.left(72)

def gwiazdy(ile, bok, krok):
    turtle.setup(1280, 720)
    turtle.bgcolor("#000000")
    turtle.fillcolor("#000000")
    turtle.pencolor("#00ffff")
    turtle.pensize(3)
    for i in range(ile):
        print(i)
        gwiazda(bok + krok * i)

def kolo(r):
    turtle.penup()
    turtle.setpos(0, -r)
    turtle.pendown()
    turtle.circle(r)

def kola(ile, r, krok):
    turtle.setup(1280, 720)
    turtle.bgcolor("#000000")
    turtle.pencolor("#00ffff")
    turtle.pensize(3)
    for i in range(ile):
        kolo(r + krok * i)
    
def main(args):
    # kwadraty(4, 100, 20)
    # gwiazdy(5, 100, 20)
    kola(5, 100, 20)
    turtle.done
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
