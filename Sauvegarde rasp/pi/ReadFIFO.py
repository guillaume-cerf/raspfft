import ADXL362bis as ADXL362
import spidev
import time
import ConversionAccelsFIFO as conv
import FuncWriteReg as write
accel=ADXL362.ADXL362()
write.Write(0x28,0x02)
accel.begin_measure()
accel.spi.cshigh=False
time.sleep(.1)
#print("FIFO watermark",accel.spi_read_reg(0x0B))
value=accel.spi.xfer2([0x0D]+[0x00]*600)[1:]
#print("FIFO watermark",accel.spi_read_reg(0x0B))
accel.spi.cshigh=True
f=open("ListAccel.txt","w")
listaccel=conv.convert(value)
print(listaccel)
f.write(str(listaccel))
f.close()
