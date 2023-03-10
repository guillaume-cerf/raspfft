import ADXL362 as ADXL362
import spidev

accel = ADXL362.ADXL362()
accel.begin_measure()
#nl=input("Nombre de lignes a lire (1 ou 2):\n")
adress=input("Ligne du registre a lire :\n")
accel.spi.cshigh=False
#if nl==1:
print(accel.spi.xfer2([0x0B,adress,0x00]))
#else:
#	print(accel.spi_read_two(adress))
accel.spi.cshigh=True
