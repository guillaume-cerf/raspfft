#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 08:45:17 2018

@author: poney
"""

import FuncWriteReg

def reglage(accel,freq):
    value=''        #variable qui va contenir l'octet que l'on veut ecrire
    if accel==2:    #####Debut des tests pour la plage de mesure
        value="00"
    elif accel==4:
        value="01"
    else:
        value="10"
    value+="010"    ####Fin des tests de plage
    ##########tests de frequence##############
    if freq==100:
        value+="011"
    elif freq==200:
        value+='100'
    else:
        value+='111'
    print(value)
    ############fin des tests de frequence#############
    print(str(hex(int(value,2))))     #conversion de binaire a hexadecimal
    FuncWriteReg.Write(0x2C,int(value,2))      #ecriture dans le registre via FuncWriteReg afin d'avoir les comparaison entre les valeurs a ecrire et les valeurs actuelles
