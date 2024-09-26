#Napiši program, ki izpiše vse delitelje podanega števila.

stevilo = int(input("Vpisi stevilo: "))

for i in range(1, stevilo+1):
    if stevilo % i == 0:
        print(i)