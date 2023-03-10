import ADXL362bis as ADXL362
import time
accel = ADXL362.ADXL362()
accel.begin_measure()
accel.spi.cshigh=False
accel.spi_write_reg(0x28,0x02)
accel.spi.cshigh=True
#print(reg)
