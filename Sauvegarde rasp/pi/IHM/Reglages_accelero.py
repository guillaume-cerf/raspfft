#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 08:45:17 2018

@author: poney
"""

import FuncWriteReg

def maj_reglages(etat_accel,etat_freq):
    '''mets a jour les reglages sur l'accelerometre'''
    
    value=''        #variable qui va contenir l'octet que l'on veut ecrire
    if etat_accel==0:    #Debut des tests pour la plage de mesure ici test 2g
        value="00"
    elif etat_accel==1: #4g
        value="01"
    else:                       #8g
        value="10"
    value+="010"    #Fin des tests de plage on ajoute les bits 'obligatoires'
    
    if etat_freq=='':   #debut tests de frequence ici pour 100Hz non dispo sur l'ihm
        value+="011"
    elif etat_freq==0: #200Hz
        value+='100'
    else:                       #400Hz
        value+='111'
    print(value) #fin des tests de frequence
    print(str(hex(int(value,2))))     #conversion de binaire a hexadecimal
    FuncWriteReg.Write(0x2C,int(value,2))      #ecriture dans le registre via FuncWriteReg afin d'avoir les comparaison entre les valeurs a ecrire et les valeurs actuelles
