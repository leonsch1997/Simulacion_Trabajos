import random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def ruleta():
    numsal=[]
    numeros=0

    for x in range(300):
        numeros=random.randint(0,36)
        numsal.append(numeros)
    return numsal

def calculaprom(numsal):
    prom = []
    acumi = 0
    acumprom = 0
    pos=1
    for y in numsal:
        acumi += y
        acumprom = acumi / pos
        prom.append(acumprom)
        pos+=1
    return prom
def prom_y_var_de_prom(prom):
    pos = 1
    promdeprom=[]
    acumi = 0
    vari = []
    for y in prom:
        acumi += y
        acumprom = acumi / pos
        promdeprom.append(acumprom)
        vari.append(np.var(prom[pos-1:pos+1]))
        pos += 1
    return[promdeprom,vari]
def frecuen (numeros):
    freqr=[]
    for y in range(37):
        freqr.append(numeros.count(y) / 300)
    return freqr
def graficar (numsal,fre,prom,promdeprom,vari):
    plt.title("Números que salieron")
    plt.hist(numsal,color = 'green', edgecolor = 'black',  linewidth=2)
    plt.show()
    plt.title("Frecuencia de los números")
    plt.plot(fre,color='red')
    plt.show()
    plt.title("Promedio de los números")
    plt.plot(prom,color='red')
    plt.show()
    plt.title("Promedio de los promedios")
    plt.plot(promdeprom,color='red')
    plt.show()
    plt.title("Varianza de los promedios")
    plt.plot(vari,color='red')
    plt.show()


rul = ruleta()
frec=frecuen(rul)
prome = calculaprom(rul)
pyvdep= prom_y_var_de_prom(prome)
promdeprom = (pyvdep[0])
vardeprom = (pyvdep[1])
graficar(rul,frec,prome,promdeprom,vardeprom)