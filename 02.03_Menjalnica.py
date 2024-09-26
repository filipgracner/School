"""3.    Menjalnica
Dijaki prvih letnikov bodo letos v času OIV obiskali Istanbul.
V šoli so jih obvestili, da morajo s seboj imeti tudi nekaj turških novih lir.
Anka se je na poti domov ustavila v menjalnici, kjer so ji povedali,
da je pri njih menjalni tečaj odvisen od količine menjalnega denarja.

Če bo menjala manj kot 50 €, bo menjalni tečaj za 1 € = 4,56  TRY.
Če bo menjala več kot ali enako 50 € pa do 200 €, bo menjalni tečaj za 1 € = 4,68 TRY.
Če pa bo menjala več kot 200 €, bo menjalni tečaj za 1 € = 4,95 TRY."""

denar = float(input("Vnesi količino denarja:"))

if denar < 50:
    menjalni_tecaj = 4.56
elif denar >= 50 and denar <= 200:
    menjalni_tecaj = 4.68
else:
    menjalni_tecaj = 4.95

zamenjan_denar = denar * menjalni_tecaj

print("Anka dobi", zamenjan_denar, ", menjalni tečaj je", menjalni_tecaj)