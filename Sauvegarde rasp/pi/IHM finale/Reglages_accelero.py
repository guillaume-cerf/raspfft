#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 08:45:17 2018

@author: poney
"""
import ADXL362
import FuncWriteReg

def maj_reglages(acc,freq,accel=ADXL362.ADXL362()):
    '''mets a jour les reglages sur l'accelerometre'''
    
    value=''        #variable qui va contenir l'octet que l'on veut ecrire
    if acc==2:    #Debut des tests pour la plage de mesure ici test 2g
        value="00"
    elif acc==4: #4g
        value="01"
    else:                       #8g
        value="10"
    value+="010"    #Fin des tests de plage on ajoute les bits 'obligatoires'
    
    if freq==100:   #debut tests de frequence ici pour 100Hz non dispo sur l'ihm
        value+="011"
    elif freq==200: #200Hz
        value+='100'
    else:                       #400Hz
        value+='111'
    print(value) #fin des tests de frequence
    print(str(hex(int(value,2))))     #conversion de binaire a hexadecimal
    FuncWriteReg.Write(0x2C,int(value,2),accel)      #ecriture dans le registre via FuncWriteReg afin d'avoir les comparaison entre les valeurs a ecrire et les valeurs actuelles
