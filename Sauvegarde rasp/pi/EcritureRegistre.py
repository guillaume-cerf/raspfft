import ADXL362bis as ADXL362
import time
adress=input("Adresse ou ecrire:\n")
value=input("valeur a ecrire (en hexa):\n")
accel = ADXL362.ADXL362()
accel.begin_measure()
accel.spi.cshigh=False
if accel.spi_read_reg(adress)==value:
	print("la valeur demandee est deja celle dans le registre")
else:
	accel.spi_write_reg(adress,value)	#ecriture a l'adresse "adress" la valeur "value" rentree plus haut
	if accel.spi_read_reg(adress)==value:
		print("la valeur {} a bien ete ecrite dans la ligne {} du registre".format(value,adress))
	else:
		print("Erreur lors de l'ecriture dans le registre")
accel.spi.cshigh=True

