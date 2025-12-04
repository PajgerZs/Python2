#5. feladat – Lista elemeinek négyzetre emelés
#Adott egy lista, készíts új listát, amely minden elem négyzetét tartalmazza.

szamok = [2,3,4,5,6,7,8,9,10]
negyzetek = []

for i in range(len(szamok)):
    negyzetek.append(szamok[i]**2)

print(f"A számok négyzetei: {negyzetek}")