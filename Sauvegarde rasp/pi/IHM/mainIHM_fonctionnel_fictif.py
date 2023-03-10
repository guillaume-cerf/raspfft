import sys #impose par QT
import os
from PyQt4.QtCore import * #impose par QT
from PyQt4.QtGui import * #impose par QT
from PyQt4 import *
#import tkinter
from page_reglages import Ui_Reglages
from page_acquisitionzaloeil import Ui_Acquisition
from numpy import linspace,sin
from numpy import fft  #OU from scipy.fftpack import fft #on fait enuite uniquement fft(blabla)
from random import *  #pour les donnees fictives

##------------ Fenetre ACQUISITION avec relations

class Interface_Acquisition(QWidget): #pour une autre fenetre, ca peut etre QDialog ou QMainWindow ou QWidget
    def __init__(self):
        QWidget.__init__(self) #Appel explicite du constructeur de la classe mere, impose par python

        #Instanciation et initialisation de l'interface Qt
        self.ui = Ui_Acquisition() #class creee par Qt METTRE UN VRAI NOM
        self.ui.setupUi(self)       #on lance la fonction definie dans la class

        #initialisation parametres
        global etat_comboBox_freq, etat_comboBox_accel   #en global pour dialoguer entre acquisition et reglages

        self.ui.checkBox_accelx.setChecked(True) #par defaut coche ---- setChecked ou setCheckState
        self.ui.checkBox_accely.setChecked(True) #par defaut coche
        self.ui.checkBox_accelz.setCheckState(False) #par defaut non coche
        self.ui.comboBox_FourrierTempo.setCurrentIndex(0) #par defaut indice 0 donc temporel
        self.ui.progressBar.setValue(0)  #pour dire quelle valeur mettre (de 0 a 100) ou .value() pour consulter
        etat_comboBox_freq = 0 #par defaut 200Hz
        etat_comboBox_accel = 0 #par defaut 2g
        
        self.T =[]  #ensemble des temps
        self.F=[]   #futur ensemble des frequences pour fft
        self.A1=[]  #ensemble des accel en x
        self.A2=[]  #ensemble des accel en y
        self.A3=[]  #ensemble des accel en z
        self.Atot=[] #equivalent sortie accelero
        self.TF1 =[] #futur ensemble des TF pour A1
        self.TF2 =[] #futur ensemble des TF pour A2
        self.TF3 =[] #futur ensemble des TF pour A3
        
        self.ui.matplotlibwidget.axes.set_title('Accelerations')
        self.ui.matplotlibwidget.axes.set_ylabel('Amplitude') #ou xscale
        self.ui.matplotlibwidget.axes.set_xlabel('t(s) ou f(Hz)')
        
        # definition relations
        self.connect(self.ui.PushButton_Fermer, SIGNAL('clicked()'), self.action_Fermer)
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
        
    def action_Nouveau(self):
        print('go nouveau')
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
        self.memorise_txt()
        os.popen("recuperation_donnees.txt")
        

        
    def action_modif_affichage(self):
        print(self.ui.checkBox_accelx.checkState()) #renvoie 0 ou 2
        print(self.ui.checkBox_accely.checkState())
        print(self.ui.checkBox_accelz.checkState())
        print(self.ui.comboBox_FourrierTempo.currentIndex())  # .currentText  ou .currentIndex(0 ou 1)
        self.afficher()


    def acquerir(self):#test matplotlib
        """a pour but d'acquerir les donnees accelero"""
        N=randint(80,100)
        tmax = 2
        fe=(N-1)/tmax
        self.T = linspace(0,tmax,N)
        self.F = linspace(0,fe,N)
        self.F=self.F[0:N//2] #on coupe a la moitie pour non redondance dans l'affichage
            

        A = self.calcul_sin(self.T) #acquisition donnees fictives
        self.A1=A[0]  #accel en x
        self.A2=A[1]
        self.A3=A[2]
        self.Atot=A[3]  #cumul accel type sortie accelero

        self.TF1=2*abs(fft.fft(self.A1))/N  #TF de l'acceleration en x
        self.TF1=self.TF1[0:N//2]
        self.TF2=2*abs(fft.fft(self.A2))/N  #TF de l'acceleration en y
        self.TF2=self.TF2[0:N//2]
        self.TF3=2*abs(fft.fft(self.A3))/N  #TF de l'acceleration en z
        self.TF3=self.TF3[0:N//2]

        for i in range(N):   ##on raccourci les nombres en CS
            self.T[i]=self.nCS(self.T[i])
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
        
    def calcul_sin(self,T):
        A1=[]
        A2=[]  #sont des intermediaires de la fonction (pas de self)
        A3=[]
        L=[]
        amplitude=[2*random(),4*random(),3*random()]
        for i in T:
            a1,a2,a3=self.nCS(amplitude[0]*sin(3*i)),self.nCS(amplitude[1]*sin(6*i+1)),self.nCS(amplitude[2]*sin(12*i+2))  #2pi/T = 3 ie T=2
            A1.append(a1)
            A2.append(a2)
            A3.append(a3)
            L.append([a1,a2,a3]) #donnees fictives accelero
        return [A1,A2,A3,L]
    
    def nCS(self,nombre):
        """reduit les chiffres signicatifs a n"""
        n=3
        facteur=10**n
        return int(facteur*nombre)/facteur
    
    def memorise_txt(self): #il faut avoir fait nouveau pour tester
        """passe les donnees dans un fichier txt"""
        fich=open('recuperation_donnees.txt','w')
        fich.write('t(s)                Ax(m/s2)            Ay(m/s2)               Az(m/s2)             F(Hz)              TF(Ax)               TF(Ay)          TF(Az)\n')
        for i in range(len(self.T)):
            a,b,c,d=str(self.T[i]),str(self.Atot[i][0]),str(self.Atot[i][1]),str(self.Atot[i][2])
            if i<len(self.F):
                e,f,g,h=str(self.F[i]),str(self.TF1[i]),str(self.TF2[i]),str(self.TF3[i])
            else:
                e,f,g,h='','','',''
            fich.write(a)
            fich.write('                ') ##avec 4 tabulations tout le temps pour bien separer et avoir un passage propre sur excel
            fich.write(b)
            fich.write('                ')
            fich.write(c)
            fich.write('                ')
            fich.write(d)
            fich.write('                ')
            fich.write(e)
            fich.write('                ')
            fich.write(f)
            fich.write('                ')
            fich.write(g)
            fich.write('                ')
            fich.write(h)
            fich.write('\n')
        fich.close()



###----------------Fenetre REGLAGES avec relations
        
class Interface_Reglages(QWidget): #pour une autre fenetre, ca peut etre QDialog ou QMainWindow ou QWidget
    def __init__(self):
        QWidget.__init__(self) #Appel explicite du constructeur de la classe mere, impose par python

        #Instanciation et initialisation de l'interface Qt
        self.ui2 = Ui_Reglages()
        self.ui2.setupUi(self)
        #initialisation combobox
        self.ui2.comboBox_freq.setCurrentIndex(etat_comboBox_freq) #pour memoriser ce qui a ete fait avant
        self.ui2.comboBox_accel.setCurrentIndex(etat_comboBox_accel)

        self.connect(self.ui2.PushButton_retour, SIGNAL('clicked()'), self.action_retour)
        self.connect(self.ui2.PushButton_valider, SIGNAL('clicked()'), self.action_valider)

    def action_retour(self):
        global interface2
        print('go retour')
        interface2=0 #sans enregistrer les modif

    def action_valider(self):
        global etat_comboBox_freq, etat_comboBox_accel, interface2
        print('go valider')
        etat_comboBox_freq = self.ui2.comboBox_freq.currentIndex()
        etat_comboBox_accel = self.ui2.comboBox_accel.currentIndex()
        print(etat_comboBox_accel)
        print(etat_comboBox_freq)
        interface2=0  #il faudra faire de vraies modif sur l'accelero
    
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
    
 