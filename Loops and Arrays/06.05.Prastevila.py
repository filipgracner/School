#Napiši program, ki preveri, če je podano število praštevilo.

stevilo = int(input("Vpisi stevilo: "))
delitelj = 0

for i in range(1, stevilo+1):
    if stevilo % i == 0:
        delitelj += 1

if delitelj > 2 or stevilo == 1:
    print(stevilo, "ni prastevilo.")
else:
    print(stevilo, "je prastevilo.")
