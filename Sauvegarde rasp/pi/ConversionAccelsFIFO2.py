import ADXL362
from FuncLectureRegistre import *


def plageacc(accel=ADXL362.ADXL362()):
    ''' Lecture du registre, lecture de la plage d'acceleration
        ne sert que si la fonction convert est appellee sans donner de plage d'acceleration(valeur par defaut)
    '''
    reg=bin(accel.ADXL362.spi_read_reg(0x2c))[2:]			#regarder si c'est une liste ou juste une valeur
    reg=('0'*(8-len(reg))+reg)[:2]  #Format 8 bits
    #Interpretation en nombre de g
    if reg=='00':
        plage=2
    elif reg=='01':
        plage=4
    else:
        plage=8
    return plage



def convert(liste,plage,offset=[0,0,0],accel=ADXL362.ADXL362()):
    '''Conversion des donnees d'acceleration du FIFO codees sur deux octets 
    pour les renvoyer en nombre de g.
    
    La liste de donnees en entree est ordonnee comme suit (1 axe sur 2octets):
    [...,xn1,xn2,yn1,yn2,zn1,zn2,x(n+1)1,...] : toujours dans l'ordre x,y,z.
    Mais il est possible que la premiere valeur ne soit pas un x, il faut donc
    rester vigilant !
    Doc : page 38 data sheet ADXL362
    '''
    
    accelConv=[]
    saturation=False		#Booleen egal a True s'il y a saturation des donnees
    mauvaisaxe=False    #Booleen a True si erreur d'axe
    
    print("liste initiale",liste)
    #On cherche le premier x:
    while not isx(liste[1]<<8) or not isy(liste[3]<<8) or not isz(liste[5]<<8):		#on teste que le bit de poids fort car c'est lui qui donne les infos sur l'axe mais on teste les 3 pour etre sur
        del(liste[:2])		#################modification pour decaler que d'un element parce qu'un 0 est detecte comme un axe x########
    accel.spi.cshigh=False
    liste+=accel.spi.xfer2([0x0D]+[0x00]*(6-len(liste)%6))[1:]
    accel.spi.cshigh=True
    #Tant qu'il reste deux valeurs, soit la valeur sur un axe a l'instant t
    while len(liste)>=6:
        #S'il manque y, ou y et z, alors on complete
        if len(liste)<6:
            #break
            print("avant",liste)
            accel.spi.cshigh=False
            print('Status',accel.spi_read_reg(accel,0x0B))
            liste+=accel.spi.xfer2([0x0D]+[0x00]*(6-len(liste)))[1:]
            accel.spi.cshigh=True
            print("apres",liste)
        
        #Extraction donnees axes
        print(liste,len(liste)%6)
        x=liste[0]+(liste[1]<<8)    #somme des deux premiers octets
        y=liste[2]+(liste[3]<<8)    #idem
        z=liste[4]+(liste[5]<<8)    #idem
        print("premieresval",x,y,z)
        while not isx(x) or not isy(y) or not isz(z):
            del(liste[:2])
            print('suppr')
            if len(liste)<6:
                accel.spi.cshigh=False
                print("avant2",liste,accel.spi_read_reg(0x0b))
                acc=accel.spi.xfer2([0x0D]+[0x00]*(6-len(liste)))	##############
                liste+=acc[1:]
                print("apres2",liste,"ajout:",acc)
                accel.spi.cshigh=True
            x=liste[0]+(liste[1]<<8)
            y=liste[2]+(liste[3]<<8)    
            z=liste[4]+(liste[5]<<8)
            print("newval",x,y,z)
        del(liste[:6])
        #Si non tous nuls:
        if [x,y,z]!=[0,0,0]:		#ne devrait plus arriver car si toutes les valeurs sont nulles, on ne passe pas le test isx,isy...
            #Est-ce bien x ?
            if not isx(x):		#On pourrait enlever ce test en theorie (aussi pour y et z) car le test est effectue en debut de boucle mais on le garde pour debuggage
                mauvaisaxe=True
                return (accelConv,saturation,mauvaisaxe)
                break
            #Est-ce negatif ?
            if x>=2**12:
                x-=2**12+2**13      #Suppression bits de signe
                x-=2**12				#Complement a deux pour passer en negatif
            #Le signal est-il sature ? (si les 11bits de data sont a 1)
            if abs(x)>=2047:
                saturation=True
            
            
            if not isy(y):
                mauvaisaxe=True
                return (accelConv,saturation,mauvaisaxe)
                break
            y-=2**14
            if y>=2**12:
                y-=2**12+2**13
                y-=2**12
            if abs(y)>=2047:
                saturation=True
            
            
            if not isz(z):
                mauvaisaxe=True
                return (accelConv,saturation,mauvaisaxe)
                break
            z-=2**15
            if z>=2**12:
                z-=2**12+2**13
                z-=2**12
            if abs(z)>=2047:
                saturation=True
        
        #Ajout triplet aux donnees partiellement converties
        accelConv.append([x,y,z])
    
    #Conversion finale en nombre de g
    accelbis=[]
    for i in accelConv:
        accelbis.append([float(i[j])*plage/2048-offset[j] for j in range(3)])
    return (accelbis,saturation,mauvaisaxe)


#Fonctions verifiant que la valeur renseignee est du bon axe
##Bits d'axe : 15 et 16
def isx(val):       #Code 00
    if val>=2**14:
        return False
    else:
        return True

def isy(val):       #Code 01
    if val>=2**15 or val-2**14<0:
        return False
    else:
        return True

def isz(val):       #Code 10
    if val-2**15<0 or val-2**14-2**15>=0:
        return False 
    else:
        return True
