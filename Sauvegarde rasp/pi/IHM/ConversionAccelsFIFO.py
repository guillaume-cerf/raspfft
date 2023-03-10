from FuncLectureRegistre import *

def plage():				#Lecture du registre pour avoir la plage d'acceleration si elle n'est pas fournie
    reg=bin(Lecture(0x2c)[0])[2:]	#on lit les parametres pour recuperer les plages d'acceleration stockees
    reg=('0'*(8-len(reg))+reg)[:2]
    if reg=='00':
        plage=2		#permet de connaitre le nombre de G pour la conversion
    elif reg=='01':
        plage=4
    else:
        plage=8
    return plage

def convert(liste,plage=plage(),i=0):		#Conversion des valeurs renvoyees par le fifo
    accel=[]
    print(liste,len(liste))
    while len(liste)>2:
        i+=1
        print(i)
        x=liste.pop(0)+liste.pop(0)*2**8    #somme des deux octets pour traitement
        while not isx(x):
            x=liste.pop(0)+liste.pop(0)*2**8    #somme des deux octets pour traitement
        y=liste.pop(0)+liste.pop(0)*2**8        #comme pour x, seules les conditions des tests changent
        z=liste.pop(0)+liste.pop(0)*2**8
        if [x,y,z]!=[0,0,0]:
            if not isx(x):
                return('la valeur {} ne correspond pas a un "x"'.format(x))
                break
            if x>=2**12:
                x-=2**12+2**13
                x-=2**12				#Complement a deux pour passer en negatif
            if not isy(y):
                return 'la valeur {} ne correspond pas a un "y"'.format(y),i 
                break
            y-=2**14
            if y>=2**12:
                y-=2**12+2**13
                y-=2**12
            if not isz(z):
                return('la valeur {} ne correspond pas a un "z"'.format(z))
                break
            z-=2**15
            if z>=2**12:
                z-=2**12+2**13
                z-=2**12
        accel.append([x,y,z])
    accelbis=[]
    for i in accel:
        accelbis.append([float(j)*plage/2048 for j in i])
    return accelbis



def isx(val):			#Teste si la valeur rensignee est bien un x
    if val>=2**14:
        return False

def isy(val):			#de meme pour y et z
    if val>=2**15 or val-2**14<0:
        return False
def isz(val):
    if z-2**15<0 or z-2**14-2**15>=0:
        return False 
