import ADXL362bis as ADXL362
import time
accel = ADXL362.ADXL362()
accel.begin_measure()
accel.spi.cshigh=False
#reg=accel.read_xyz()
reg=accel.check_all_regs()
accel.spi.cshigh=True
print(reg)
