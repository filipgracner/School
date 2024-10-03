"""Napišite program, ki za dani seznam poišče zmagovalca v izštevanki "An ban pet podgan".
V vsakem odštevanju izpade tisti, na katerega pokažemo ob besedi “ven”. Zmagovalec igre
je tisti, ki na koncu edini ostane neizločen.
Za preverjanje: če imamo osebe ["Maja", "Janja", "Sabina", "Ina",
"Jasna"] je zmagovalec Jasna. Če izštevamo osebe ["Maja", "Janja",
"Sabina"], zmaga Maja.
Za tiste, ki ste že malo pozabili; celotna izštevanka se glasi: 'an ban, pet podgan, štiri miši,
v uh me piši, vija, vaja, ven.'"""

osebe = ["Maja", "Janja", "Sabina", "Ina", "Jasna"]

for i in range(len(osebe)-1):
    ven = 11 % len(osebe)
    osebe.pop(ven-1)
    print("Ostale osebe po", str(i+1) + ". krogu:")
    print(osebe)

zmagovalka = osebe[0]
print("Zmagovalka je", zmagovalka.upper() + "!")
