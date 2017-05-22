import tkinter as tk
import random

     
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

class Matrika:

    def __init__(self, matrika,okno):
        self.matrika=matrika
        self.slika = tk.Canvas(okno, bg='white',height=400,width =400)
        self.slika.place(relx=.35,rely=.5)

    def osvezi(self):
        self.slika.delete('all')
        for i in range(4):
            for j in range(4):
                self.slika.create_text(j*100+50,i*100+50)
        
def dodaj_dve(matrika):
    stevilo_nicel=0
    for i in range(4):
        for j in range(4):
            if matrika[i][j] ==0:
                stevilo_nicel += 1
    k = random.randint(1,stevilo_nicel)
    nova_matrika =[]
    stevilo_nicel =0
    for i in range(4):
        vrstica = []
        for j in range(4):
            if matrika[i][j] ==0:
                stevilo_nicel += 1
                if stevilo_nicel ==k:
                    vrstica.append(2)
                else:
                    vrstica.append(0)
            else:
                vrstica.append(matrika[i][j])
        nova_matrika.append(vrstica)
    return nova_matrika
       

def transponiraj(matrika):
    transponirana = []
    for i in range(4):
        vrstica = []
        for j in range(4):
            vrstica.append(matrika[j][i])
        transponirana.append(vrstica)
    return transponirana
    
def skrci_matriko(matrika,smer):
    matrika2 = []
    if smer ==1:
        for i in range(4):
            matrika2.append(skrci_levo(matrika[i]))
        return matrika2
    elif smer ==2:
        for i in range(4):
            matrika2.append(skrci_desno(matrika[i]))
        return matrika2
    elif smer ==3: #skrci gor
        return transponiraj(skrci_matriko(transponiraj(matrika),1))
    elif smer == 4:
        return transponiraj(skrci_matriko(transponiraj(matrika),2))

def skrci_levo_brez_nicel(s):
    if len(s)<=1:
        return s
    elif s[0]!=s[1]:
        return [s[0]] + skrci_levo_brez_nicel(s[1:])
    else:
        return [2*s[0]] + skrci_levo_brez_nicel(s[2:])

def skrci_levo(s):
    seznam =[]
    for i in s:
        if i !=0:
            seznam.append(i)
    seznam = skrci_levo_brez_nicel(seznam)
    return seznam + [0]*(len(s)-len(seznam)) 

def skrci_desno(s):
    return skrci_levo(s[::-1])

matrika = Matrika([[2,5,4,1],[5,2,6,548],[5,8,9,84],[15,85,24,2]],okno)
matrika.osvezi()

okno.mainloop()
        
