"""Napiši program, ki vrne najmanjše pozitivno število v seznamu. Negativna števila in 0 naj prezira. Če v seznamu ni
pozitivnih števil, naj to izpiše."""

stevila = [0, 4, -1, -3, 9, 13, 2]
min_check = False

for i in range(len(stevila)):
    if stevila[i] > 0:
        min_poz = stevila[i]
        min_check = True
        print("st", min_poz)
        break

if min_check == False:
    print("V seznamu ni pozitivnega števila.")
else:
    for i in range(len(stevila)):
        if stevila[i] < min_poz and stevila[i] > 0:
            min_poz = stevila[i]
    print("Najmanjse stevilo v seznamu je", min_poz)