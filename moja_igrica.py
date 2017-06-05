import tkinter as tk
import random

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
    return skrci_levo(s[::-1])[::-1]

class Matrika:

    def __init__(self,okno):
        self.slika = tk.Canvas(okno, bg='white',height=400,width =400)
        self.slika.place(relx=.35,rely=.5)
        self.nova_igra()
        okno.bind('<Left>',self.levi_klik)
        okno.bind('<Right>',self.desni_klik)
        okno.bind('<Up>',self.gor_klik)
        okno.bind('<Down>',self.dol_klik)

    def osvezi(self):
        self.slika.delete('all')
        for i in range(4):
            for j in range(4):
                self.narisi_polje(i,j)
                
    def narisi_polje(self,i,j):
        barve = ['lemon chiffon','beige','wheat','sandy brown', 'coral','tomato','orange red', 'red','pink','hot pink','deep pink']
        stevilo = self.matrika[i][j]
        if stevilo==2:
            barva = barve[0]
        elif stevilo==4:
            barva = barve[1]
        elif stevilo==8:
            barva = barve[2]
        elif stevilo==16:
            barva = barve[3]
        elif stevilo==32:
            barva = barve[4]
        elif stevilo==64:
            barva = barve[5]
        elif stevilo==128:
            barva = barve[6]
        elif stevilo==256:
            barva = barve[7]
        elif stevilo==512:
            barva = barve[8]
        elif stevilo==1024:
            barva = barve[9]
        elif stevilo==2048:
            barva = barve[10]
        if stevilo != 0:
            self.slika.create_polygon(100*j+5,100*i+5,100*(j+1)-5,100*i+5,100*(j+1)-5,100*(i+1)-5,100*j+5,100*(i+1)-5,fill=barva)
            self.slika.create_text(j*100+50,i*100+50,text=str(stevilo),font='arial 20')

    def nova_igra(self):
        self.matrika = dodaj_dve([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
        self.osvezi()
        
    def levi_klik(self,event):
        matrika2= skrci_matriko(self.matrika,1)
        if matrika2 != self.matrika:
            self.matrika=matrika2
            self.matrika = dodaj_dve(self.matrika)
        else:
            stevilo_nicel=0
            for i in range(4):
                for j in range(4):
                    if self.matrika[i][j] ==0:
                        stevilo_nicel+= 1
            if stevilo_nicel==0:
                self.slika.create_text(100,100,text='IZGUBILI STE!',font='arial 30')
        self.osvezi()
        
    def desni_klik(self,event):
        matrika2= skrci_matriko(self.matrika,2)
        if matrika2 != self.matrika:
            self.matrika=matrika2
            self.matrika = dodaj_dve(self.matrika)
        else:
            stevilo_nicel=0
            for i in range(4):
                for j in range(4):
                    if self.matrika[i][j] ==0:
                        stevilo_nicel+= 1
            if stevilo_nicel==0:
                self.slika.create_text(100,100,text='IZGUBILI STE!',font='arial 30')
        self.osvezi()
        
    def gor_klik(self,event):
        matrika2= skrci_matriko(self.matrika,3)
        if matrika2 != self.matrika:
            self.matrika=matrika2
            self.matrika = dodaj_dve(self.matrika)
        else:
            stevilo_nicel=0
            for i in range(4):
                for j in range(4):
                    if self.matrika[i][j] ==0:
                        stevilo_nicel+= 1
            if stevilo_nicel==0:
                self.slika.create_text(100,100,text='IZGUBILI STE!',font='arial 30')
        self.osvezi()
        
    def dol_klik(self,event):
        matrika2= skrci_matriko(self.matrika,4)
        if matrika2 != self.matrika:
            self.matrika=matrika2
            self.matrika = dodaj_dve(self.matrika)
        else:
            stevilo_nicel=0
            for i in range(4):
                for j in range(4):
                    if self.matrika[i][j] ==0:
                        stevilo_nicel+= 1
            if stevilo_nicel==0:
                self.slika.create_text(100,100,text='IZGUBILI STE!',font='arial 30')
        self.osvezi()      
          
okno = tk.Tk()

gumbi= tk.Frame(okno)
ime_igre = tk.Label(okno, text = '2048')
ime_igre.place(relx=.01,rely=.01)
sestevek_tock = tk.Label(okno, text ='sestevek: ')
sestevek_tock.place(relx=.7,rely=.01)    
matrika = Matrika(okno)
gumb_nova_igra = tk.Button(okno,text = 'Nova igra',command = matrika.nova_igra)
gumb_nova_igra.place(relx=.32,rely=.09)
gumb_najboljsi_rezultat = tk.Button(okno,text = 'Najboljsi rezultat')
gumb_najboljsi_rezultat.place(relx=.7,rely=.09)
okno.title("2048")


okno.mainloop()
        
