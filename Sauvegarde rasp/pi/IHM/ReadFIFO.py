import ADXL362 as ADXL362
import spidev
import time
import ConversionAccelsFIFO as conv
import FuncWriteReg as write

def go():
    
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
    f.write(str(value))
    print(conv.convert(value))
    f.close()

    return value     #qui permet de recup la liste dans le main
