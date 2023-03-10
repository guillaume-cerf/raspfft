import sys #impose par QT
import os
from PyQt4.QtCore import * #impose par QT
from PyQt4.QtGui import * #impose par QT
from PyQt4 import *
import time  #pour nommer le fichier txt final


from page_reglagesv2 import Ui_Reglages
from page_acquisitionzaloeilv2 import Ui_Acquisition
from numpy import linspace
from numpy import fft  #OU from scipy.fftpack import fft #on fait enuite uniquement fft(blabla)

#pour l'accelero :
import Reglages_accelero         #nom du fichier python dont la fonction maj_reglages permet d'ecrire dans le registre les nouveaux reglages
import FIFO                 #FIFO.go() permet d'enregistrer le fifo
from FuncWriteReg import Write
import ADXL362
import Offset

##------------ Fenetre ACQUISITION avec relations

class Interface_Acquisition(QWidget): #pour une autre fenetre, ca peut etre QDialog ou QMainWindow ou QWidget
    def __init__(self):
        QWidget.__init__(self) #Appel explicite du constructeur de la classe mere, impose par python

        #Instanciation et initialisation de l'interface Qt
        self.ui = Ui_Acquisition() #class creee par Qt METTRE UN VRAI NOM
        self.ui.setupUi(self)       #on lance la fonction definie dans la class
        
        
        #initialisation parametres
        global etat_comboBox_freq, etat_comboBox_accel,etat_comboBox_nbech, begin,accelero  #en global pour dialoguer entre acquisition et reglages

        self.ui.checkBox_accelx.setChecked(True) #par defaut coche ---- setChecked ou setCheckState
        self.ui.checkBox_accely.setChecked(True) #par defaut coche
        self.ui.checkBox_accelz.setCheckState(False) #par defaut non coche
        self.ui.comboBox_FourrierTempo.setCurrentIndex(0) #par defaut indice 0 donc temporel
        self.ui.progressBar.setValue(0)  #pour dire quelle valeur mettre (de 0 a 100) ou .value() pour consulter
        etat_comboBox_freq = 0 #par defaut 200Hz
        etat_comboBox_accel = 0 #par defaut 2g
        etat_comboBox_nbech = 0 #par defaut 128
        
        begin=True  #on commence
        self.offset=False
        accelero=ADXL362.ADXL362()  #initialisation de l'accelerometre
        Write(0x28,2)       #activation du FIFO et desactivation de la temperature

        self.init_listes() #initialise une premiere fois les listes
        self.afficher() #pour un premier affichage du matplotlib vide mais avec legende etc

        self.action_Reglages() #on part directement sur la page reglages (apres on revient et les relations sont crees)
        
        # definition relations
        self.connect(self.ui.PushButton_Fermer, SIGNAL('clicked()'), self.action_Fermer)
        self.connect(self.ui.PushButton_Init, SIGNAL('clicked()'), self.action_initialisation)
        self.connect(self.ui.PushButton_Nouveau, SIGNAL('clicked()'), self.action_Nouveau)
        self.connect(self.ui.PushButton_Reglages, SIGNAL('clicked()'), self.action_Reglages)
        self.connect(self.ui.PushButton_Exporter, SIGNAL('clicked()'), self.action_Exporter)
        self.connect(self.ui.comboBox_FourrierTempo, SIGNAL('currentIndexChanged(int)'), self.action_modif_affichage)
        self.connect(self.ui.checkBox_accelx, SIGNAL('clicked()'), self.action_modif_affichage) #ou stateChanged(int)
        self.connect(self.ui.checkBox_accely, SIGNAL('clicked()'), self.action_modif_affichage)
        self.connect(self.ui.checkBox_accelz, SIGNAL('clicked()'), self.action_modif_affichage)
        
        
    def action_Fermer(self):
        global interface
        print('go fermer')
        interface=0 #sans espace
        
    def action_initialisation(self):
        '''prends l'offset quand on clique sur initialisation'''
        global accelero
        self.ui.progressBar.setValue(0)

        self.init_listes() #initialise les listes
        self.afficher()
        
        self.valoffset = Offset.offset(100,param[0],accelero) #pour enlever la composante statique

        self.ui.progressBar.setValue(100)
        time.sleep(2) #on attend 1s avant de remettre a 0
        self.ui.progressBar.setValue(0)
        self.offset=True #on a bien pris l'offset
        print("prise de l'offset : ",self.valoffset)
        
    def action_Nouveau(self):
        print('go nouveau')
        if self.offset: #si on a fait l'offset
            self.ui.progressBar.setValue(0) #mise a 0
            self.acquerir()    
            self.afficher()
            self.ui.progressBar.setValue(100) #mise a 100 fictive
        
    def action_Reglages(self):
        global interface2
        print('go reglages')
        interface2 = Interface_Reglages()
        interface2.show()
        
    def action_Exporter(self):
        print('go exporter')
        self.name = '/home/pi/Documents/Mesures/'+time.strftime("%d:%m:%Y-%T")+'.txt' # creation nom fichier txt avec jj:mm:aaaa-h:min:s
        print('adresse fichier : ',self.name)
        self.memorise_txt()
        self.name = 'leafpad '+self.name
        print(self.name)
        os.system(self.name)  #pour ouvrir le fichier txt cree, l'utilisateur fait enregistrer sous sa cle usb
        
        
    def action_modif_affichage(self):
        print(self.ui.checkBox_accelx.checkState()) #renvoie 0 ou 2
        print(self.ui.checkBox_accely.checkState())
        print(self.ui.checkBox_accelz.checkState())
        print(self.ui.comboBox_FourrierTempo.currentIndex())  # .currentText  ou .currentIndex(0 ou 1)
        self.afficher()


    def acquerir(self):
        """a pour but d'acquerir les donnees accelero et les rend fonctionnelles"""
        global param, accelero
        #declenchement par amplitude avant
        
        self.init_listes() #on reinitialise les 3 listes d'accel
        
        self.ui.progressBar.setValue(25)      
        Atot,saturation,mauvaisaxe = FIFO.FIFO(param[2],param[0],self.valoffset,accelero) #liste des triplets issus du fifo (384/2/3 = 64 donnees par axe)
        self.ui.progressBar.setValue(75)
        
        N=len(Atot) #nb triplets mesures
        print('Nb triplets acquis =',N)
        fe = param[1]   #on prend freq echant
        tmax = (N-1)/fe
        
        self.T = linspace(0,tmax,N)
        self.F = linspace(0,fe,N)
        self.F=self.F[0:N//2] #on coupe a la moitie Shannon

        for i in range(N):
            self.A1.append(Atot[i][0])  #ecriture accel en x
            self.A2.append(Atot[i][1])
            self.A3.append(Atot[i][2])

        self.TF1=2*abs(fft.fft(self.A1))/N  #TF de l'acceleration en x
        self.TF1=self.TF1[0:N//2]
        self.TF2=2*abs(fft.fft(self.A2))/N  #TF de l'acceleration en y
        self.TF2=self.TF2[0:N//2]
        self.TF3=2*abs(fft.fft(self.A3))/N  #TF de l'acceleration en z
        self.TF3=self.TF3[0:N//2]

        for i in range(N):   ##on raccourci les nombres en CS --- (INUTILE SI ENTIERS)
            self.T[i]=self.nCS(self.T[i])
            self.A1[i]=self.nCS(self.A1[i])
            self.A2[i]=self.nCS(self.A2[i])
            self.A3[i]=self.nCS(self.A3[i])
            if i<N//2:
                self.F[i]=self.nCS(self.F[i])
                self.TF1[i]=self.nCS(self.TF1[i])
                self.TF2[i]=self.nCS(self.TF2[i])
                self.TF3[i]=self.nCS(self.TF3[i])
        
    def afficher(self):
        """affiche le graphe avec les courbes choisies"""
        self.X1=[]
        self.X2=[]
        self.X3=[]
        self.Y1=[] #on affichera tout le temps X1,X2,X3,Y1,Y2,Y3 quitte a etre vide, sont nos variables d'affiachage
        self.Y2=[]
        self.Y3=[]
        self.c1=self.ui.checkBox_accelx.checkState() #lecture etat checkbox 0 ou 2
        self.c2=self.ui.checkBox_accely.checkState()
        self.c3=self.ui.checkBox_accelz.checkState()
        self.c4=self.ui.comboBox_FourrierTempo.currentIndex() #1 pour Fourrier et 0 pour temporel
        
        if self.c1==2 and self.c4==0:  #si accelx coche et temporel
            self.Y1=self.A1
            self.X1=self.T
        if self.c2==2 and self.c4==0:
            self.Y2=self.A2
            self.X2=self.T
        if self.c3==2 and self.c4==0:
            self.Y3=self.A3
            self.X3=self.T

        if self.c1==2 and self.c4==1:  #si accelx coche et Fourrier
            self.Y1=self.TF1
            self.X1=self.F
        if self.c2==2 and self.c4==1:
            self.Y2=self.TF2
            self.X2=self.F
        if self.c3==2 and self.c4==1:
            self.Y3=self.TF3
            self.X3=self.F

            
        self.ui.matplotlibwidget.axes.hold(False) #on tej le plot precedent et n'est pas ce qui supprime les titres  
        self.ui.matplotlibwidget.axes.plot(self.X1,self.Y1,'r-')   # . pour avoir les points et - pour les relier --> par exemple'r.-'  
        self.ui.matplotlibwidget.axes.hold(True) #on maintient
        self.ui.matplotlibwidget.axes.plot(self.X2,self.Y2,'b-')
        self.ui.matplotlibwidget.axes.hold(True)
        self.ui.matplotlibwidget.axes.plot(self.X3,self.Y3,'g-')
        
        self.ui.matplotlibwidget.axes.set_title('Accelerations') #a repeter car supprimer par le replot
        self.ui.matplotlibwidget.axes.set_ylabel('Amplitude') #ou xscale
        self.ui.matplotlibwidget.axes.set_xlabel('t(s) ou f(Hz)')
        
        self.ui.matplotlibwidget.draw() ##important
        
    
    
    
    def memorise_txt(self): #il faut avoir fait nouveau pour tester
        """passe les donnees dans un fichier txt"""
        global param        
        fich=open(self.name,'w') #defini dans action_exporter
        fich.write('gamme acceleration : +-')
        fich.write(str(param[0]))
        fich.write('g ;    frequence echantillonnage : ')
        fich.write(str(param[1]))
        fich.write('Hz ;   Nombre de triplets [x,y,z] : ')
        fich.write(str(param[2]))
        fich.write('t(s);Ax(g);Ay(g);Az(g);F(Hz);TF(Ax);TF(Ay);TF(Az)\n')
        for i in range(len(self.T)):
            a,b,c,d=str(self.T[i]),str(self.A1[i]),str(self.A2[i]),str(self.A3[i])
            if i<len(self.F):
                e,f,g,h=str(self.F[i]),str(self.TF1[i]),str(self.TF2[i]),str(self.TF3[i])
            else:
                e,f,g,h='','','',''
            a,b,c,d,e,f,g,h=a.replace('.',','),b.replace('.',','),c.replace('.',','),d.replace('.',','),e.replace('.',','),f.replace('.',','),g.replace('.',','),h.replace('.',',') #on remplace . en , pour traitement excel
            fich.write(a)
            fich.write(';') ##avec ; tout le temps pour bien separer et avoir un passage propre sur excel
            fich.write(b)
            fich.write(';')
            fich.write(c)
            fich.write(';')
            fich.write(d)
            fich.write(';')
            fich.write(e)
            fich.write(';')
            fich.write(f)
            fich.write(';')
            fich.write(g)
            fich.write(';')
            fich.write(h)
            fich.write('\n')
        fich.close()


    def init_listes(self):
        '''initialise toutes les listes pour pouvoir les reecrire pour chaque nouveau'''

        self.T =[]  #ensemble des temps
        self.F=[]   #futur ensemble des frequences pour fft
        self.A1=[]  #ensemble des accel en x
        self.A2=[]  #ensemble des accel en y
        self.A3=[]  #ensemble des accel en z
        self.TF1 =[] #futur ensemble des TF pour A1
        self.TF2 =[] #futur ensemble des TF pour A2
        self.TF3 =[] #futur ensemble des TF pour A3

    
        
 
    def nCS(self,nombre):     ##### INUTILE SI ON TRAITE DES NOMBRES ENTIERS OU AVEC PEU DE DECIMALES
        """reduit les chiffres signicatifs a n"""
        n=3
        facteur=10**n
        return int(facteur*nombre)/facteur

    


#time.localtime()[0] pour avoir l'annee ou time.time() pour avoir le temps (s depuis 40 ans)



          


###----------------Fenetre REGLAGES avec relations
        
class Interface_Reglages(QWidget): #pour une autre fenetre, ca peut etre QDialog ou QMainWindow ou QWidget
    def __init__(self):
        global begin
        QWidget.__init__(self) #Appel explicite du constructeur de la classe mere, impose par python
        
        #Instanciation et initialisation de l'interface Qt
        self.ui2 = Ui_Reglages()
        self.ui2.setupUi(self)

        if begin: #si c'est le premier affichage des reglages on change le nom et plus tard la fonctionnalite du bouton retour
            self.ui2.PushButton_retour.setText("Fermer")
            
        #initialisation combobox
        self.ui2.comboBox_freq.setCurrentIndex(etat_comboBox_freq) #pour memoriser ce qui a ete fait avant
        self.ui2.comboBox_accel.setCurrentIndex(etat_comboBox_accel)

        self.action_maj_affichage() #init de l'affichage
        
        self.connect(self.ui2.PushButton_retour, SIGNAL('clicked()'), self.action_retour)
        self.connect(self.ui2.PushButton_valider, SIGNAL('clicked()'), self.action_valider)
        self.connect(self.ui2.comboBox_freq, SIGNAL('currentIndexChanged(int)'), self.action_maj_affichage)
        self.connect(self.ui2.comboBox_nbech, SIGNAL('currentIndexChanged(int)'), self.action_maj_affichage)

    def action_retour(self):
        global interface2, begin, interface
        print('go retour')
        if not(begin):   #si on ne commence pas on peut faire retour
            interface2=0 #sans enregistrer les modif
        else:           #si on commence, retour est equivalent a quitter tout
            interface=0
            interface2=0
        print(begin)

    def action_valider(self):
        global etat_comboBox_freq, etat_comboBox_accel,etat_comboBox_nbech, interface2, begin, param, accelero
        print('go valider')
        etat_comboBox_freq = self.ui2.comboBox_freq.currentIndex()
        etat_comboBox_accel = self.ui2.comboBox_accel.currentIndex()
        etat_comboBox_nbech = self.ui2.comboBox_nbech.currentIndex()
        print(etat_comboBox_accel)
        print(etat_comboBox_freq)
        print(etat_comboBox_nbech)

        param = self.interpretation_param(etat_comboBox_accel,etat_comboBox_freq,etat_comboBox_nbech) #au cas ou on ne change que l'accel on ne passe pas par action_modif_affichage
        
        Reglages_accelero.maj_reglages(param[0],param[1],accelero)  #on met a jour les reglages de l'accelero

        begin=False   #on a donc fait un premier reglage
        

        interface2=0

    def action_maj_affichage(self):
        '''met a jour l'affichage quand on change les valeurs des comboboxs'''
        global param
        param = self.interpretation_param(self.ui2.comboBox_accel.currentIndex(),self.ui2.comboBox_freq.currentIndex(),self.ui2.comboBox_nbech.currentIndex())
        valfmax=str(int(param[1]/2/1.28))+' Hz'
        resolution=str(int(100*param[1]/param[2])/100)+' Hz' #precision au 1/100 Hz
        self.ui2.label_valfmax.setText(valfmax)
        self.ui2.label_valresolution.setText(resolution)
        print(valfmax)
        print(resolution)

    def interpretation_param(self,comboBox_accel,comboBox_freq,comboBox_nbech): #en argument pour ne pas toucher aux etats_comBox_ de maniere definitive
        '''donne [accel,freq,nbech]'''
        param=[]
        #test accel
        if comboBox_accel==0:  #2g
            accel=2
        elif comboBox_accel==1:  #4g
            accel=4
        else:
            accel=8
        #test freq
        if comboBox_freq==0: #100Hz
            freq=100
        elif comboBox_freq==1: #200Hz
            freq=200
        else:                       #400Hz
            freq=400
        #test nbech    
        if comboBox_nbech==0: #128 points
            nbech=128
        elif comboBox_nbech==1:
            nbech=256
        elif comboBox_nbech==2:
            nbech=512
        else:
            nbech=1024
        param.append(accel)
        param.append(freq)
        param.append(nbech)

        print(param)
        return param
    
###Reglages.showFullScreen()
###Reglages.showMaximized()

#C:\Users\cyril\Downloads\WinPython-32bit-3.3.5.9\python-3.3.5\Lib\site-packages\PyQt4\doc\html   qcheckbox etc    



###------------- Lesture du MAIN pour lancer l'algo

#Test de l'application
if __name__=="__main__":
    appUI = QApplication(sys.argv) #Instanciation de l'application (pour intercepter les mouvements de souris etc...)
    interface = Interface_Acquisition() #Instanciation de l'interface
    #interface = Interface_Reglages()  #l'un ou l'autre pour les tests
    ##interface.resize(680,320)
    ##interface.showMaximized()  ##pas utile car n'est lu qu'une fois
    interface.show() #Affichage de l'interface
    sys.exit(appUI.exec_()) #Execution de l'application
    
 
