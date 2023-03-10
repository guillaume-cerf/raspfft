import ADXL362
import spidev

accel = ADXL362.ADXL362()
accel.begin_measure()


#************************Lecture************************#
adress=input("Ligne du registre a lire :\n")
accel.spi.cshigh=False                  #Met la Chip en stand-by
val=accel.spi_read_reg(adress)          #Lecture des donnees, val en decimal
accel.spi.cshigh=True
print("Valeur lue :\n",val)             #Affichage non interprete en decimal

val=bin(val)[2:]                    #Conv en binaire en retirant le '0b'
val='0'*(8-len(val))+val            #Complete sur 8 bits


#********************Interpretation********************#
#Permet d'interpreter les lignes 0x0B, 0x28, 0x2C et 0x2D soit respectivement
#le Status Register, le FIFO Control, le Filter Control et le Power Control
#(voir donneesii pour plus de details)
if adress==0x0B :
    donnees0B=["ERR_USER_REGS","AWAKE","INACT","ACT","FIFO_OVERRUN","FIFO_WATERMARK","FIFO_READY","DATA_READY"]
    for i in range(len(donnees0B)):
        print(donnees0B[i]+" : ", bool(int(val[i])))

elif adress==0x28 :
    donnees28=["Abode Half","FIFO_Temperature","FIFO_MODE"]
    fifoModes=["Disabled","Oldest saved mode","Stream mode","Triggered mode"]
    for i in range(len(donnees28)):
        if i==2:
            print(donnees28[i]+" : ", fifoModes[int(val[-2:],2)])
        else:
            print(donnees28[i]+" : ", bool(int(val[4+i])))

elif adress==0x2C :
    donnees2C=["RANGE","HALF_BANDWIDTH","EXT_SAMPLE","FREQ"]
    rangeAcc=[2,4,8,8]
    Freq=[12.5,25,50,100,200,400,400,400]
    for i in range(len(donnees2C)):
        if i==0:
            print(donnees2C[i]+' : +-', rangeAcc[int(val[:2],2)])
        elif i==3:
            print(donnees2C[i]+' : ', Freq[int(val[-3:],2)])
        else:
            print(donnees2C[i]+" : ", bool(int(val[2+i])))

elif adress==0x2D :
    donnees2D=["EXT_CLK","LOW_NOISE","WAKEUP","AUTOSLEEP","MEASURE"]
    bruit=['Normal','Low','UltraLow','(reserved)']
    measure=['standby','(reserved)','measurement','(reserved)']
    for i in range(len(donnees2D)):
        if i==0:
            print(donnees2D[i]+" : ", bool(int(val[i])))
        elif i==1:
            print(donnees2D[i]+' : ', bruit[int(val[2:4],2)])
        elif i==4:
            print(donnees2D[i]+' : ', measure[int(val[-2:],2)])
        else:
            print(donnees2D[i]+" : ", bool(int(val[2+i])))


