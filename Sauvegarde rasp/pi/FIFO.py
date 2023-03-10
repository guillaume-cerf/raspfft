import ADXL362
import time
import ConversionAccelsFIFO as conv
import Watermark
import FuncWriteReg as fwr

def FIFO(nbPointsNecessaires, plageaccel,offset,accel=ADXL362.ADXL362()):
    '''Extraction des donnees d'acceleration suivant x,y,z. Celle-ci s'effectue
    des que la limite de remplissage, le watermark, est atteint.
    L'enregistrement n'est fait que quand le seuil est depasse.
    On envoie ensuite tout ce qui est extrait vers la fonction de conversion
    pour obtenir des valeurs en nombre de g.
    '''
    
    listeAcc=[]                     #Liste renvoyee
    wmk=Watermark.watermarkRead(accel)   #Valeur limite remplissage FIFO
    saturation = False              #Detection saturation acceleration
    problemeAxe = False             #Detection probleme d'axe
    seuil = False                   #Detection seuil
    n=20                            #Nombre donnees conservees avant activation seuil
    #print('Status',accel.spi_read_reg(0x0B))
    accel.spi_write_reg(0x1F,0x00)
    #print('Status',accel.spi_read_reg(0x0B))
    
    #Tant que la liste n'est pas pleine et qu'aucun probleme de mesure n'est detecte
    while len(listeAcc)<nbPointsNecessaires and not saturation:
        accel.spi.cshigh=False              #Met la Chip en stand-by
        status=accel.spi_read_reg(0x0B)     #Lecture du status
        accel.spi.cshigh=True
        #Watermark atteint ? (en booleen)
        besoinLecture=Watermark.watermark(bin(status)[2:])
        
        #Si le watermark est atteint il faut vider le FIFO jusqu'au watermark
        if besoinLecture :
            #Lecture ensemble donnees, multiple de 6
            accel.spi.cshigh=False
            values=accel.spi.xfer2([0x0D]+[0x00]*(wmk-wmk%6-6))[1:]
            accel.spi.cshigh=True
            
            #Suppression des series de 0 de fin de lecture, inutile si tout va bien
            while values[-2:]==[0]*2:
                del(values[-6:])
            
            #Conversion des donnees en g
            conversion,saturation,problemeAxeInstant=conv.convert(values,plageaccel,accel,offset)
            
            listeAcc+=conversion
            
            #Detection seuil si jamais apparu avant
            if not seuil:
                i=0
                while i<len(conversion) and not seuil:
                    #Depasse 10% de la valeur max ?
                    if (conversion[i][0]**2+conversion[i][1]**2+conversion[i][2]**2)**0.5>=0.1*plageaccel:
                        seuil = True
                        #Conservation de x=20 donnees avant seuil
                        listeAcc=listeAcc[-len(conversion)+(i-n):]
                    i+=1	
                if i==len(conversion) and not seuil:
                    listeAcc=listeAcc[-n:]
            
            #Y a-t'il deja eu une erreur d'axe ?
            problemeAxe=bool(problemeAxe+problemeAxeInstant)
            
            #Laisse le temps au FIFO de se remplir legerement
            time.sleep(.05)
            
    #Conservation du bon nobre de donnees
    if len(listeAcc)>nbPointsNecessaires:
        listeAcc=listeAcc[0:nbPointsNecessaires]
    return(listeAcc, saturation, problemeAxe)
