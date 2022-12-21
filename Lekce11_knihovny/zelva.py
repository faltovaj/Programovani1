"""
Zelvi grafika - modul turtle
Priklad: ctvercova spirala
Prikazy pro zelvu:
forward(10): pohyb o 10 pixelu dopredu
backward(10): pohyb o 10 pixelu dozadu
right(35): otoceni po smeru hodin. rucicek, 35 - uhel ve stupnich
left(35): otoceni proti smeru hodin. rucicek
penup(): zvednuti pera
pendown(): pero dolu
goto(x,y): posun na pozici (x,y)
home(): presun do stredu
"""
# Nacteme moduly turtle a random
import turtle
# Modul random pro nahodny vyber barvy (neni nutne)
import random

# t je objekt typu Turtle (zelva)
t = turtle.Turtle()
# Kurzor se bude vykreslovat jako zelva
t.shape('turtle')

# Barvy tuzky zelvy
barvy = ['red','green','blue','cyan','black','brown','yellow']

# Ukazka: vykresleni ctverce
n = 4
for i in range(0,n):
    # Vybereme nahodne barvu, kterou nakreslime hranu
    t.pencolor(random.choice(barvy))
    # pohyb dopredu o zvetsujici se cislo
    t.forward(200)
    # otoceni proti smeru hodinovych rucicek o 90 stupnu
    t.left(90)

# Ukonceni zelvy
turtle.done()
