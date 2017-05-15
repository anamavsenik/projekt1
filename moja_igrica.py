import tkinter as tk
from random import *

okno = tk.Tk()
gumbi=tk.Frame(okno)
ime_igre = tk.Label(okno, text = '2048')
ime_igre.place(relx=.01,rely=.01)
sestevek_tock = tk.Label(okno, text ='sestevek: ')
sestevek_tock.place(relx=.7,rely=.01)
gumb_nova_igra = tk.Button(okno,text = 'Nova igra')
gumb_nova_igra.place(relx=.32,rely=.08)
okno.title("2048")


ozadje_okna=tk.Canvas(okno, bg="pink", height=50, width=50)
ozadje_okna.place(relx=.35,rely=.5)

class Okence:
    def __init__(self,slika,i,j,cifra = 0):
        self.cifra =cifra
        a=slika.width()//4
#        b=slika.winfo_height()//4
        a,b=5,5
        slika.create_polygon(i*a,j*b,i*a+a,j*b,i*a+a,j*b+b,i*a,j*b+b,fill='red')
s=Okence(ozadje_okna,0,0,cifra = 0)






okno.mainloop()
        
