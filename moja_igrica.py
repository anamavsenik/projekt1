import tkinter as tk
from random import *


#class Okno      
okno = tk.Tk()
gumbi= tk.Frame(okno)
ime_igre = tk.Label(okno, text = '2048')
ime_igre.place(relx=.01,rely=.01)
sestevek_tock = tk.Label(okno, text ='sestevek: ')
sestevek_tock.place(relx=.7,rely=.01)
gumb_nova_igra = tk.Button(okno,text = 'Nova igra')
gumb_nova_igra.place(relx=.32,rely=.09)
gumb_najboljsi_rezultat = tk.Button(okno,text = 'Najboljsi rezultat')
gumb_najboljsi_rezultat.place(relx=.7,rely=.09)
okno.title("2048")

#class Tabela
def __init__(self, vrstice=5,stolpci=5):
    self.tabela = []
    for vrstica in range(vrstice):
        do_sedaj = []
        for stolpec in range(stolpci):
            label = Label(self, text = 0, borderwidth = 20, width = 2, font = ( 16) )
            label.grid(row = vrstica, column = stolpec, sticky = "nsew", padx = 1, pady = 1)#sticky je poravnava w je npr west
            do_sedaj.append(label) #tukaj spremeni še barvo robu tabele
        self.tabela.append(do_sedaj)

    
    
ozadje_okna=tk.Canvas(okno, bg="pink", height=50, width=50)
ozadje_okna.place(relx=.35,rely=.5)

class Okence:
    def __init__(self,slika,i,j,cifra = 0):
        self.cifra =cifra
 #       a=slika.width()//4
#        b=slika.winfo_height()//4
        a,b=5,5
        slika.create_polygon(i*a,j*b,i*a+a,j*b,i*a+a,j*b+b,i*a,j*b+b,fill='red')
s=Okence(ozadje_okna,0,0,cifra = 0)



okno.mainloop()
        
