from tkinter import *

def say():
    print('hi')





fenetre=Tk()
label = Label(fenetre,text='Hello WORD',bg='red',fg='blue',width=30)
label.pack()
print("bonjour")
#fenetre.update()
print('2')
bouton=Button(fenetre, text='Fermer',command=quit)
bouton.pack()

bouton2=Button(fenetre,text='Cou²',command=say)
bouton2.pack()

value=StringVar()
value.set('text ?')
entree=Entry(fenetre, textvariable=value, width=60)
entree.pack()

bouton3=Checkbutton(fenetre, text='Nouveau')
bouton3.pack()

value=StringVar()
bouton4=Radiobutton(fenetre, text='??',variable=value, value=1)
bouton4.pack()


###while 1:
##    i+=1
##    #fenetre.update()
##    print(i)
##    fenetre.mainloop()
##    #fenetre.destroy()

