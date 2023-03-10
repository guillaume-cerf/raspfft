############################################################
### Example for Communicating with ADXL362 Accelerometer ###
### for Raspberry Pi using ADXL362.py                    ###
###                                                      ###
### Authors: Sam Zeckendorf                              ###
###          Nathan Tarrh                                ###
###    Date: 3/29/2014                                   ###
############################################################

import ADXL362bis as ADXL362
import time

accel = ADXL362.ADXL362()
accel.begin_measure()
i=0
f=open("ListeAccel.txt",'w')
while i<256:
    f.write(str(accel.read_xyz()))
    f.write("\n")
    i=i+1
f.close()
