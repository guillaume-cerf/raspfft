import ADXL362
import spidev

def Lecture(adress,accel=ADXL362.ADXL362()):
    accel.begin_measure()
    accel.spi.cshigh=False
    return accel.spi.xfer2([0x0B,adress,0x00])[2:]
    accel.spi.cshigh=True
