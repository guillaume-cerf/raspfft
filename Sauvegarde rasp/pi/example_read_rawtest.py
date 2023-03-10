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
accel.spi.cshigh=False
i=0
while i<100:
    i+=1
    print(accel.spi.xfer2([0x0B,0x12,0x00,0x00]))
    time.sleep(1/512)
accel.spi.cshigh=True
