"""Napiši funkcijo najvec_n(s, n), ki kot argument prejme seznam s in
največje dovoljeno število ponovitev elementov na seznamu, n. Funkcija naj vrne nov seznam,
v katerem se vsak element pojavi
največ n-krat, vse nadaljnje ponovitve pa se pobrišejo."""

stevila = [1, 2, 3, 3, 2, 2, 2, 2, 1, 1, 5, 8, 6, 6, 2, 5, 4, 3, 2, 4, 5, 3, 2, 5, 6, 6, 4]
najvec_ponovitev = int(input("Kolikokrat se lahko posamezno stevilo ponovi? "))

def najvec_n(seznam, naj_pon):
    odstranjena_st = 0
    uniq_num = []
    stevila_ok = seznam.copy()
    for i in range(len(stevila)):
        if stevila[i] not in uniq_num:
            uniq_num.append(stevila[i])
            
    naj_stevec = 0
    for i in range(len(uniq_num)):
        for j in range(len(seznam)):
            if seznam[j] == uniq_num[i]:
                naj_stevec += 1
                if naj_stevec > naj_pon:
                    stevila_ok.pop(j-odstranjena_st)
                    odstranjena_st += 1
        naj_stevec = 0   
    return stevila_ok 

print(najvec_n(stevila, najvec_ponovitev))
