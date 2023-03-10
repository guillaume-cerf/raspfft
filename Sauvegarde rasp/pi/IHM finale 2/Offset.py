# -*- coding: utf-8 -*-
"""
Created on Fri May  4 14:51:54 2018

@author: El Jeton 180-107 An 216
"""

import ADXL362
from ConversionAccelsFIFO import convert
import FIFO



def offset(nbVals,plageaccel,accel=ADXL362.ADXL362()):
    '''Permet de definir l'offset, soit la mesure de l'attraction terrestre
    pour une position fixe de l'accelerometre
    '''
    print('Initialisation en cours, please wait...')    #Idealement visuel IHM
    x=0
    y=0
    z=0
    Listeaccel,satur,pbaxe=FIFO.FIFO(nbVals,plageaccel,[0,0,0],accel)
    for i in Listeaccel:			#On parcours la liste des accelerations renvoyees (normalement en statique) et on ajoute les valeurs correspondantes sur chaque axe pour pouvoir en faire la moyenne
        x+=i[0]
        y+=i[1]
        z+=i[2]    
    return [x/nbVals,y/nbVals,z/nbVals] #renvoi de la moyenne
