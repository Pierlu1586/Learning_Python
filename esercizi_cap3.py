#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 18:40:09 2023

@author: Pierluigi Mastroianni
"""

# =============================================================================
# Esercizi 3.14
# =============================================================================

# Esercizio 3.1

# =============================================================================
# def giustif_destra(s):
#     str = ''
#     for i in range(70-len(s)):
#         str = str + ' '
# 
#     print(str+s)
# 
# 
# giustif_destra('monty')
# =============================================================================
                                                                
# Esercizio 3.2

#1
# =============================================================================
# def fai2volte(f):
#     f()
#     f()
#     
# def stampa_spam():
#     print('spam')
#     
# fai2volte(stampa_spam)
# =============================================================================

#2

# =============================================================================
# def fai2volte(f, value):
#     f(value)
#     f(value)
#  
# def stampa_valore(val):
#     print(val)
#      
# fai2volte(stampa_valore, 'Prova')
# =============================================================================

#3

# =============================================================================
# def fai2volte(f, value):
#     f(value)
#     f(value)
#   
# def stampa2volte(bruce):
#     print(bruce)
#     print(bruce)
#       
# fai2volte(stampa2volte, 'spam')
# =============================================================================

#4

def fai_quattro(f, value):
    f(value)
    f(value)
   
def stampa2volte(bruce):
    print(bruce)
    print(bruce)
       
fai_quattro(stampa2volte, 'spam')