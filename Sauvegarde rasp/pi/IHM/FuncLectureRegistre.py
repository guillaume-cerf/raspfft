import ADXL362 as ADXL362
import spidev

accel = ADXL362.ADXL362()
def Lecture(adress):
    accel.begin_measure()
    accel.spi.cshigh=False
    return accel.spi.xfer2([0x0B,adress,0x00])[2:]
    accel.spi.cshigh=True
