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

#4 *** CORRETTO *** 

# =============================================================================
# def fai_quattro(f, value):
#     fai2volte(f, value)
#     fai2volte(f, value)
#    
# def fai2volte(function, bruce):
#     function(bruce)
#     function(bruce)
#        
# fai_quattro(print, 'test')
# =============================================================================

# Esercizio 3.3.1

# Versione 1
# =============================================================================
# def disegnaGriglia():
#     for i in range(2):
#         print('+','-','-','-','-','+','-','-','-','-','+')
#         for i in range(4):    
#             print('|'+'         '+'|'+'         '+'|')
#     print('+','-','-','-','-','+','-','-','-','-','+')
# =============================================================================
    
# Versione 2 - migliorata [Sviluppo per riga] ***MIGLIORABILE***


# =============================================================================
# def addHSegment():
#     print('+', end='')
#     print(' -'*4, end=' ')
#   
# def closeHSegment():
#     print('+')
#     
# def addVSegment():
#     print('|', end=' '*9)
# 
# def closeVSegment():
#     print('|')
#     
# def createHLine():
#     addHSegment()
#     addHSegment()
#     closeHSegment()
#     
# def createVLine():
#     addVSegment()
#     addVSegment()
#     closeVSegment()
#     
# def doFour(f):
#     f()
#     f()
#     f()
#     f()
#     
# 
# def disegnaGriglia2X2():
#     createHLine()
#     doFour(createVLine)
#     createHLine()
#     doFour(createVLine)
#     createHLine()
# 
#     
# disegnaGriglia2X2()
# =============================================================================


# Esercizio 3.3.2
# Ulteriore miglioramento del codice - Disegno griglia 4X4  

def addHSegment():
    print('+', end='')
    print(' -'*4, end=' ')
  
def closeHSegment():
    print('+')
    
def addVSegment():
    print('|', end=' '*9)

def closeVSegment():
    print('|')
    
def doFour(f):
    f()
    f()
    f()
    f()
    
def createEntireVLine():
    doFour(addVSegment)
    closeVSegment()
    
def createEntireHLine():    
    doFour(addHSegment)
    closeHSegment()    

def drawRow():
    createEntireHLine()
    doFour(createEntireVLine)

def disegnaGriglia4X4():
    doFour(drawRow)
    createEntireHLine()
    
disegnaGriglia4X4()
    