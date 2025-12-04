#2. feladat – Kérj be egy N számot, és számold ki az 1-től N-ig terjedő számok szorzatát
#(faktoriális ELLENTÉTE: itt nem csak N!, hanem általánosan 1·2·3…·N).

n = int(input("Kérem az egész számot: "))
szorzas = 1

for i in range(1, n+1):
    szorzas *=i

print(f"Az 1-től {n}-ig terjedő számok szorzata {szorzas} lesz.")