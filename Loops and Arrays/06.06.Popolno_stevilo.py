"""Število je popolno, če je enako vsoti svojih deliteljev (razen samega sebe). Primer popolnega števila je 28, ki ga
delijo 1, 2, 4, 7, in 14: če jih seštejemo, spet dobimo 28.
Napiši program preveri, če je podano število popolno."""

stevilo = int(input("Vnesi stevilo: "))
vsota = 0

for i in range(1, stevilo):
    if stevilo % i == 0:
        vsota += i

if stevilo == 0:
    print(stevilo, "ni popolno stevilo")
elif vsota == stevilo:
    print("Stevilo je popolno")
else:
    print("Stevilo ni popolno. Vsota njegovih deliteljev (razen samega sebe) je", vsota)