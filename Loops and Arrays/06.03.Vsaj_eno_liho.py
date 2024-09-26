#Napiši program, ki prejme seznam števil in pregleda, če je med njimi vsaj eno liho.

stevila = [0, -1, 5, 102, 53, -67]
liho = False

for i in range(len(stevila)):
    if stevila[i] % 2 == 1:
        liho = True
        break

if liho == False:
    print("V seznamu ni lihega stevila")
else:
    print("Seznam vsebuje vsaj eno liho stevilo")