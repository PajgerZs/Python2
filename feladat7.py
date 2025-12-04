#7. feladat – OOP: Egyszerű Osztály – Auto
#Hozz létre egy Auto osztályt, amely attribútumai: márka, típus, évjárat
#Az osztály tartalmazzon metódust, ami kiírja a teljes adatot szép formában.

class Auto:
    def __init__(self, marka, tipus, evjarat):
        self.marka = marka
        self.tipus = tipus
        self.evjarat = evjarat

    def kiir(self):
        print(f"{self.marka}, {self.tipus}, {self.evjarat}")

auto1 = Auto("VW","Bora","2002")
auto2 = Auto("Ford","Focus","2011")

print(auto1.kiir())
print(auto2.kiir())