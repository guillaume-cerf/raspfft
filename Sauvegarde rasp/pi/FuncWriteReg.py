#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 08:08:52 2018

@author: poney
"""
import ADXL362bis as ADXL362

def Write(adress,value,accel=ADXL362.ADXL362()):        #la valeur doit etre en hexadecimal!!!!!!!!!!
    accel.begin_measure()
    accel.spi.cshigh=False
    if accel.spi_read_reg(adress)==value:       #on compare la valeur que l'on veut ecrire avec celle deja dans le registre afin de ne pas ecrire pour rien
	print("equal")
    	return "equal"
    else:
    	accel.spi_write_reg(adress,value)	#ecriture a l'adresse "adress" la valeur "value" rentree plus haut
    	if accel.spi_read_reg(adress)==value:
    	    print("OK")	
            return "OK"
    	else:
                print("NOK")
    		return "NOK"
    accel.spi.cshigh=True
