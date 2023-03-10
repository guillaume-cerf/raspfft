import ADXL362bis as ADXL362
import spidev
import time
import ConversionAccelsFIFO as conv
accel=ADXL362.ADXL362()
accel.begin_measure()
while True:
    accel.spi.cshigh=False
    time.sleep(.01)
    value=accel.spi.xfer2([0x0D,0x00,0x00,0x00,0x00,0x00,0x00])[1:]
    accel.spi.cshigh=True
    time.sleep(.01)
    print(value)#conv.convert(value))

