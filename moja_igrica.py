import Tkinter as tk
import random

stevec = 0

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
    global stevec
    global sestevek_tock

    if len(s)<=1:
        return s
    elif s[0]!=s[1]:
        return [s[0]] + skrci_levo_brez_nicel(s[1:])
    else:
        res = 2*s[0]
        stevec = stevec + res
        sestevek_tock.config(text = "sestevek: {}".format(stevec))
        return [res] + skrci_levo_brez_nicel(s[2:])

def zapisi_rezultat():
    f = open('rezultati.txt', 'a')
    f.write(',' + str(stevec))
    f.close()
    
def preberi_najboljsi_rezultat():
    tabela = []
    with open('rezultati.txt', 'r') as f:
        for line in f:
            for word in line.split(','):
                tabela.append(int(word))
    max = 0
    for i in range(len(tabela)):
        if max < tabela[i]:
            max = tabela[i]
    return str(max)

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
        self.slika.place(relx=.01,rely=.15)
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
        barve = ['peach puff','hot pink','deep pink','medium orchid', 'dark violet','seashell4','bisque4','cornflower blue','deep sky blue', 'blue','cyan']
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
        global stevec
        global sestevek_tock

        self.matrika = dodaj_dve([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])

        stevec = 0
        sestevek_tock.config(text = "sestevek: {}".format(stevec))
        self.osvezi()
        
    def levi_klik(self,event):
        self.matrika = skrci_matriko(self.matrika,1)
        self.matrika = dodaj_dve(self.matrika)
        self.osvezi()
        
    def desni_klik(self,event):
        self.matrika = skrci_matriko(self.matrika,2)
        self.matrika = dodaj_dve(self.matrika)
        self.osvezi()
        
    def gor_klik(self,event):
        self.matrika = skrci_matriko(self.matrika,3)
        self.matrika = dodaj_dve(self.matrika)
        self.osvezi()
        
        
    def dol_klik(self,event):
        self.matrika = skrci_matriko(self.matrika,4)
        self.matrika = dodaj_dve(self.matrika)
        self.osvezi()


okno = tk.Tk()
gumbi= tk.Frame(okno)
ime_igre = tk.Label(okno, text = '2048',font='arial 20')
ime_igre.place(relx=.02,rely=.01)
sestevek_tock = tk.Label(okno, text ='sestevek: {}'.format(stevec), font='arial 12')
sestevek_tock.place(relx=.7,rely=.01)    
matrika = Matrika(okno)
gumb_nova_igra = tk.Button(okno,text = 'Nova igra',command = matrika.nova_igra)
gumb_nova_igra.place(relx=.02,rely=.09)
gumb_najboljsi_rezultat = tk.Label(okno,text = 'Najboljsi rezultat : ' + preberi_najboljsi_rezultat(),font='arial 12')
gumb_najboljsi_rezultat.place(relx=.55,rely=.09)
stanje = tk.Label(okno, text ='', font='arial 18')
stanje.place(relx=.25 ,rely=.02)
okno.title("2048")

okno.geometry('{}x{}'.format(410, 500))
okno.mainloop()
