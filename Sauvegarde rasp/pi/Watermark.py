# -*- coding: utf-8 -*-
"""
Created on Fri May 18 09:15:36 2018

@author: Utilisateur
"""
import ADXL362
import spidev
import FuncWriteReg



def watermark(status):
    return(bool(status[-3]))

def waterWrite(value,accel=ADXL362.ADXL362()):  #value en decimal
    #conversion en binaire
    ##Half Above (9e bit)
    HA=False
    if value - 2^8 >=0:         #Si value type 1 XXXXXXXX
        HA=True
        value-=2**8
    accel.spi.cshigh=False
    mesure0x28=accel.spi_read_reg(0x28)         #Lecture des donnees en 0x28
    accel.spi.cshigh=True
    mes0x28bin=bin(mesure0x28)[2:]    #Conv en binaire en retirant le '0b'
    mes0x28bin='0'*(8-len(mes0x28bin))+mes0x28bin      #Etendu a 8 bits
    #Ecriture de HA sans changer les autres valeurs du registre
    FuncWriteReg.Write(0x28,mesure0x28[0:4]+str(1*HA)+mesure0x28[5:])
    
    ##dernier octet
    FuncWriteReg.Write(0x29,value)

def watermarkRead(accel=ADXL362.ADXL362()):
    accel.spi.cshigh=False
    mesure0x28=bin(accel.spi_read_reg(0x28))[2:]         #Lecture des donnees en 0x28
    mesure0x28='0'*(8-len(mesure0x28))+mesure0x28
    mesure0x29=accel.spi_read_reg(0x29)         #Lecture des donnees en 0x29
    accel.spi.cshigh=True
    
    return((int(mesure0x28[-4],2)<<8)+mesure0x29)
