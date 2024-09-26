"""Ocenjevanje zaposlenih
V podjetju UČINKOVITOST d.o.o. zaposleni ob koncu vsakega leta dobijo oceno.
Ocenjevalna lestvica se začne pri 0,0 in sega do 1,0.
0,0 – 0,39               nesprejemljiva učinkovitost
0,4 – 0,59               sprejemljiva učinkovitost
0,6 ali več               nadpovprečna učinkovitost
Od ocene je odvisna tudi plača zaposlenih. Plača se izračuna kot produkt ocene in 2400 €.
Napišite program, ki bo prebral številsko oceno zaposlenega in izpisal njegovo opisno oceno in višino plače,
ki jo na podlagi ocene dobi.
Če vpisana ocena ni med 0,0 in 1,0, naj program izpiše »Ocena je napačna!«
Primer: Vpiši oceno: 0,73
               Tvoja ocena: nadpovprečna učinkovitost, višina plače: 1752 €."""



ocena = float(input("Vpiši oceno delavca:"))
while(ocena < 0.0 or ocena > 1.0):
    print("Ocena je napačna!")
    ocena = float(input("Vpiši oceno:"))

placa = 2400 * ocena
if ocena >= 0.4 and ocena <= 0.59:
    opisna_ocena = "sprejemljiva učinkovitost"
elif ocena >= 0.6 and ocena <= 1.0:
    opisna_ocena = "nadpovprečna učinkovitost"
else:
    opisna_ocena = "nesprejemljiva učinkovitost"


print("Tvoja ocena:", opisna_ocena, ", višina plače:",placa, "€." )
