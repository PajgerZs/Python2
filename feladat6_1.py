emberek = {}

for i in range(2):
    lista = []
    nev = input("Kérem a nevet: ")
    kor = input("Kérem az életkorát: ")
    lista.append(kor)
    hajszin = input("Kérem a hajszínt: ")
    lista.append(hajszin)
    emberek[nev] = lista

max = 0
i = 0
for x in emberek:
    if emberek[x][0] > int(max):
        max = int(emberek[x][0])
        i = x

print(f"A legidősebb ember neve {i}, az értékei pedig {emberek[i]}")