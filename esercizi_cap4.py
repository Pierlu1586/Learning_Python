#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 17:20:13 2023

@author: Pierluigi Mastroianni
"""

import turtle
import math
bob = turtle.Turtle()
print(bob)

# bob.fd(200)
# bob.lt(90)
# bob.fd(200)
# turtle.mainloop()

# Istruzioni per disegnare un quadrato di 200px di lato 

# =============================================================================
# QUADRATO di 200px  DISEGNATO CON 'ELENCO DI COMANDI'
# bob.fd(200)
# bob.lt(90)
# bob.fd(200)
# bob.lt(90)
# bob.fd(200)
# bob.lt(90)
# bob.fd(200)
# turtle.mainloop()
# =============================================================================

# =============================================================================
# CON CICLO FOR
# for i in range(4):
#     bob.fd(200)
#     bob.lt(90)
# 
# turtle.mainloop()
# =============================================================================


# =============================================================================
# ESERCIZIO 4.3.1
# def quadrato(t):
#     for i in range(4):
#         t.fd(100)
#         t.lt(90)
#         
# quadrato(bob)
#         
# turtle.mainloop()
# =============================================================================


# =============================================================================
# ESERCIZIO 4.3.2
# def quadrato(t, lunghezza):
#     for i in range(4):
#         t.fd(lunghezza)
#         t.lt(90)
#         
# quadrato(bob, 100)
# 
# turtle.mainloop()
# =============================================================================


# =============================================================================
# ESERCIZIO 4.3.3
# def poligono(t, lunghezza, n):
#       for i in range(n):
#           t.fd(lunghezza)
#           t.lt(360/n)
#         
# poligono(bob, 5, 200)
# 
# turtle.mainloop()
# 
# =============================================================================



# =============================================================================
# ESERCIZIO 4.3.4
# def poligono(t, lunghezza, n):
#     """Metodo per costruire dei poligoni regolari"""
#     for i in range(n):
#         t.fd(lunghezza)
#         t.lt(360/n)
#           
# def cerchio(t,r):
#     circ = 2*math.pi*r
#     numeroLati = 200
#     lungLato = circ/numeroLati
#     poligono(t,lungLato,numeroLati)
#     
# cerchio(bob, 200)    
# =============================================================================


# =============================================================================
# ESERCIZIO 4.3.5
# def poligono(t, lunghezza, n, a):
#     """Metodo per costruire dei poligoni regolari"""
#     for i in range(n):
#         t.fd(lunghezza)
#         t.lt(a/n)
#           
# def arco(t,r,a):
#      t.lt(90)
#      circ = 2*math.pi*r
#      numeroLati = 200
#      lungLato = (circ/numeroLati)/3
#      poligono(t,lungLato,numeroLati, a)
#     
# arco(bob, 200, 60)
# =============================================================================

def quadrato(tart, lunghezza):
    for i in range(4):
        tart.fd(lunghezza)
        tart.lt(90)

#quadrato(bob, 50)

def poligono(tart, lunghezza, n, ang):
    for i in range(n):
        tart.fd(lunghezza)
        #dà l'angolo ad ognuno degli nlati da disegnare, questo è ottenuto dividendo l'arco da renderizzare
        # diviso il numero di lati utilizzati per disegnare l'arco
        tart.lt(ang/n)  

# poligono(bob, 100, 8)

def cerchio(tart, raggio):
    circonferenza = 2*math.pi*raggio
    numeroLati = 200
    arcoCirc = circonferenza/numeroLati
    poligono(tart,arcoCirc,numeroLati)

#cerchio(bob, 50)

def arco(tart, raggio, angolo):
    tart.lt(90) #ruota tartaruga di 90 gradi
    circonferenza = 2*math.pi*raggio #mi calcola la circonferenza
    rad = (math.pi*angolo)/180 #converte gli angoli in radianti
    nlati = int(circonferenza/rad) #determina il numero approssimativo di lati per il poligono da circ e rad 
    poligono(tart,rad,nlati,angolo)
    
arco(bob, 100, 60)    

turtle.mainloop()

    