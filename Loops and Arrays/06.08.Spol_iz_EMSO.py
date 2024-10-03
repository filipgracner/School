"""Številka EMŠO je sestavljena iz trinajst števk v obliki DDMMLLL50NNNX, pri čemer je DDMMLLL rojstni datum, 50
je koda registra, NNN je zaporedna številka in X kontrolna številka. Trimestna številka, NNN, je med 000 in 499 za
moške ter med 500 in 999 za ženske.
Napiši program ki preverja, ali podan EMŠO, pripada ženski ali moškemu. EMŠO je podan kot tabela, turej vsaka
števka je en element tabele."""

emso = [0, 5, 0, 6, 0, 0, 4, 5, 5, 1, 1, 4, 7]

if emso[8] >= 0 and emso[8] <= 4:
    spol = "moski"
elif emso[8] >= 5 and emso[8] <= 9:
    spol = "zenski"
else:
    spol = "neveljavno"

print("Spol osebe, katere EMŠO je podan, je", spol)
