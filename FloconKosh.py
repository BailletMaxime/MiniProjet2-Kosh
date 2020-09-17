from turtle import*

ordre=int(input("Choisir l'étape de formation du flocon (de 0 à 3):"))
longueur=float(input("Choisir la longueur du côté du triangle de base:"))

def fractale(t,n):
    if n<=0:
        forward(t)
        
    else:
        fractale(t/3,n-1)
        left(60)
        fractale(t/3,n-1)
        right(120)
        fractale(t/3,n-1)
        left(60)
        fractale(t/3,n-1)


def FloconKosh(t,n):
    fractale(t,n)
    right(120)
    fractale(t,n)
    right(120)
    fractale(t,n)

FloconKosh(longueur,ordre)