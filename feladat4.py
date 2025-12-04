#4. feladat – Számjegyek összege
#Kérj be egy számot, majd számold ki a számjegyeinek összegét.

n = input("Kérem az egész számot: ")
osszeg = 0

for i in range(len(n)):
    osszeg = osszeg + int(n[i])

print(f"A számjegyek összege: {osszeg}")