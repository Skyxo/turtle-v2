from turtle import *
from math import *
from random import *
from tkinter import *

def bloc(bloc_color):               #Etage d'un bâtiment
    fillcolor(bloc_color)
    begin_fill()
    for i in range(2):
        fd(140)
        left(90)
        fd(60)
        left(90)
    end_fill()

def window():                          #Fenêtre des bâtiments
    fillcolor("white")
    begin_fill()
    for i in range(4):
        fd(30)
        left(90)
    end_fill()

def door1(door_color):           #Modèle 1 de porte d'entrée ou de la porte-fenêtre
    fillcolor(door_color)
    begin_fill()
    for i in range(2):
        fd(30)
        left(90)
        fd(50)
        left(90)
    end_fill()

def door2(door_color):           #Modèle 2 de porte d'entrée
    fillcolor(door_color)
    begin_fill()
    fd(30)
    left(90)
    fd(50)
    left(90)
    right(atan(5/15)*180/pi)
    fd(sqrt(5**2+15**2))
    left(2*(atan(5/15)*180/pi))
    fd(sqrt(5**2+15**2))
    left(90-atan(5/15)*180/pi)
    fd(50)
    left(90)
    end_fill()

def door3(door_color):           #Modèle 3 de porte d'entrée
    fillcolor(door_color)
    begin_fill()
    fd(30)
    left(90)
    fd(40)
    circle(15,180)
    fd(40)
    left(90)
    end_fill()

def toit1(roof_color):              #Modèle 1 de toit
    angle = atan(50/80)*180/pi
    L = sqrt(50**2+80**2)
    fillcolor(roof_color)
    begin_fill()
    fd(150)
    left(180)
    right(angle)
    fd(L)
    left(2*angle)
    fd(L)
    left(180)
    right(angle)
    fd(10)
    end_fill()

def toit2(roof_color):              #Modèle 2 de toit
    angle = atan(2)*180/pi
    L = sqrt(5**2+10**2)

    fillcolor(roof_color)
    begin_fill()
    for i in range(2):
        fd(140)
        left(90)
        right(angle)
        fd(L)
        left(2*angle)
        fd(L)
        left(90-angle)
    end_fill()

def poutre1():                         #Petite poutre pour le balcon
    fillcolor("black")
    begin_fill()
    for i in range(2):
        fd(1)
        left(90)
        fd(30)
        left(90)
    end_fill()

def poutre2():                         #Grosse poutre pour le balcon
    fillcolor("black")
    begin_fill()
    for i in range(2):
        fd(41)
        left(90)
        fd(2)
        left(90)
    end_fill()

def balcon():                           #Balcon fenêtre
    fillcolor("black")
    begin_fill()
    up()
    xbase1 = xcor()
    ybase1 = ycor()
    setx(xcor()-5)
    sety(ycor()-20)
    xbase2 = xcor()
    down()
    poutre2()
    for i in range(11):
        poutre1()
        if i != 10:
            fd(4)
    up()
    setx(xbase2)
    sety(ycor()+29)
    down()
    poutre2()
    end_fill()
    up()
    setx(xbase1)
    sety(ybase1)
    down()

def immeuble(level, roof):      #Génération d'un immeuble
    bloc_color = (randint(0,255),randint(0,255),randint(0,255))
    door_color = (randint(0,255),randint(0,255),randint(0,255))
    roof_color = (randint(0,255),randint(0,255),randint(0,255))
    door_position = randint(0,2)

    for i in range(level):                  #corps de l'immeuble
        bloc(bloc_color)
        sety(ycor()+60)
    if roof:                                       #toit de l'immeuble
        toit1(roof_color)
    else:
        toit2(roof_color)

    sety(ycor()-level*60)
    setx(xcor()+15)
    for i in range(3):                        #porte de l'immeuble
        if door_position == i:
            door = randint(0,2)
            if door == 0:
                door1(door_color)
            elif door == 1:
                door2(door_color)
            else:
                door3(door_color)
        else:                                     #fenêtres aux rez-de-chaussé
            up()
            sety(ycor()+20)
            down()
            window()
            up()
            sety(ycor()-20)
            down()
        if i != 2:                               #repositionnement
            setx(xcor()+40)
    setx(xcor()-95)

    up()
    sety(ycor()+60)
    down()

    for i in range(level-1):            #fenêtres et portes-fenêtres de l'immeuble
        up()
        sety(ycor()+20)
        setx(xcor()+15)
        down()
        for o in range(3):
            win = randint(0,3)
            if win:
                window()                     #fenêtre
            else:
                sety(ycor()-20)
                door1("white")            #porte-fenêtre
                sety(ycor()+20)
                balcon()                      #balcon de la porte-fenêtre
            if o != 2:
                up()
                setx(xcor()+40)
                down()
        up()
        setx(xcor()-95)                    #repositionnement
        sety(ycor()-20)
        sety(ycor()+60)

def ville():                               #Fonction principale (génération de la ville)
    batiments = int(input("Combien voulez-vous de bâtiments ? (max conseillé : 10 bâtiments) : "))
    title("Construction d'une ville aléatoirement")
    hideturtle()
    colormode(255)
    speed("fastest")
    up()
    sety(ycor()+20)
    setx(-90*5)
    down()
    for i in range(batiments):       #construction des bâtiments
        level = randint(1,5)
        roof = randint(0,1)
        immeuble(level, roof)
        if i != 4:                             #retour à la ligne au bout de 5 bâtiments (sinon débordement)
            up()
            sety(ycor()-level*60)
            setx(xcor()+180)
            down()
        else:
            up()
            sety(-360)
            setx(-90*5)
            down()
    input()                                 #blocage de l'image

ville()