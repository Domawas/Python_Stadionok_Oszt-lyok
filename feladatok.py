from datetime import datetime
from Stadion import Stadion
import filebeolvasas
def newyork_stad(stadionok):
    nyc_stadionok=0
    for i in range(0,len(stadionok),1):
        if stadionok[i].varos=="New York":
            nyc_stadionok+=1
    return nyc_stadionok

def ossz_csapat(stadionok):
    csapatszam=0
    for i in range(0,len(stadionok),1):
        csapatszam+=stadionok[i].csapatok_szama
    return csapatszam

def listazas(stadionok):
    lista=[]
    for i in range(0,len(stadionok),1):
        if datetime.strptime("1900-01-01","%Y-%m-%d")>stadionok[i].elso_merk:
            lista.append(stadionok[i].nev)
    return lista

def buffalo(stadionok):
    csapat_buffalo=0
    for i in range(0,len(stadionok),1):
        if (stadionok[i].varos == "Buffalo"):
            csapat_buffalo += stadionok[i].csapatok_szama
    return csapat_buffalo