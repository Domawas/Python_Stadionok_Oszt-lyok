from Stadion import Stadion
import feladatok
import filebeolvasas

stadionok=filebeolvasas.beolvas("stadionok.txt",[])
print(stadionok)
for i in range(0,len(stadionok),1):
    print(stadionok[i])


print(f"Utolsó Mérkőzés: {stadionok[0].utolso_merk}")

e=feladatok.newyork_stad(stadionok)
print(f"New Yorkban: {e} stadion található")

e=feladatok.ossz_csapat(stadionok)
print(f"Az összes csapatszám: {e}")

e= feladatok.listazas(stadionok)
print(f"1900.01.01 előtt volt az első mérkőzésük:\n"
      f"{e}\n")

e=feladatok.buffalo(stadionok)
print(f"Összesen {e} játszott Buffaloban")