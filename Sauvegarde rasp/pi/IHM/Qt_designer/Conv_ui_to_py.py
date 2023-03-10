from PyQt4 import uic 
fin = open('C:\\Users\cyril\Documents\ENSAM_PC\GIE2\Projet Raspberry\Programmation\IHM\Qt_designer\page_reglages.ui','r')
fout = open('C:\\Users\cyril\Documents\ENSAM_PC\GIE2\Projet Raspberry\Programmation\IHM\page_reglages.py','w')
uic.compileUi(fin,fout,execute=False)
fin.close()
fout.close()
