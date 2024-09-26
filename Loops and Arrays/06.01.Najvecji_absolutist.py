"""Napiši program, ki vrne največje število po absolutni vrednosti (-8 je po absolutni vrednosti
večje od -2 in od 5) v danem seznamu. Negativna števila spremeniš v pozitivna tako, da jih množiš z -1."""

stevila = [-9, 6, 4, 2, 5, 2]
max_st = stevila[0]

for i in range(len(stevila)):
    if stevila[i] < 0:
        stevila[i] *= -1
    if stevila[i] > max_st:
        max_st = stevila[i]

print("Najvecje stevilo iz seznama je", max_st)    
