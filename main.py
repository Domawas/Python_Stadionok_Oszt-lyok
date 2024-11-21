from Stadion import Stadion

import filebeolvasas

stadionok=filebeolvasas.beolvas("stadionok.txt",[])
print(stadionok)
for i in range(0,len(stadionok),1):
    """print(stadionok[i])"""

print(f"Utolsó Mérkőzés: {stadionok[0].utolso_merk}")