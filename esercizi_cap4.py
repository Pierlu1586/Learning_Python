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
# QUADRATO DISEGNATO CON 'ELENCO DI COMANDI'
# bob.fd(200)
# bob.lt(90)
# bob.fd(200)
# bob.lt(90)
# bob.fd(200)
# bob.lt(90)
# bob.fd(200)
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


# ESERCIZIO 4.3.3
def poligono(t, lunghezza, n):
      for i in range(n):
          t.fd(lunghezza)
          t.lt(360/n)
        
poligono(bob, 5, 200)

turtle.mainloop()



# =============================================================================
# def poligono(t, lunghezza, n):
#     """Metodo per costruire dei poligoni regolari"""
#     for i in range(n):
#         t.fd(lunghezza)
#         t.lt(360/n)
#           
# def cerchio(t,r):
#     circ = 2*math.pi*r
#     
#     poligono(t,,)
#     
#     
# turtle.mainloop()
# =============================================================================
    