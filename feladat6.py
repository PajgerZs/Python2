#6. feladat – Szótár gyakorlás
#Kérj be 5 nevet és életkort, majd tárold őket egy dict-ben.
#Ezután írd ki a legidősebb személy nevét.

emberek = {}

for i in range(5):
    nev = input("Kérem a nevet: ")
    kor = input("Kérem az életkorát: ")
    emberek[nev] = kor

print(f"A legidősebb személy: {max(emberek)}")