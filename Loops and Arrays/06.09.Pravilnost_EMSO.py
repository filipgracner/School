"""Zadnja števka v EMŠO je kontrolna. Izračuna se takole: prvo števko EMŠO pomnožimo s 7, drugo s šest, tretjo s
pet in tako naprej, do šeste, ki jo pomnožimo z 2. Sedmo spet pomnožimo s 7, osmo s 6, deveto s 5 in tako do
dvanajste, ki jo pomnožimo z 2. Za zadnjo, trinajsto števko, velja tole: če jo prištejemo h gornji vsoti, dobimo
število, ki je deljivo z 11.
DDMMLLL50NNNX
Napiši program, ki preveri pravilnost podane številke EMŠO."""

emso = [0, 5, 0, 6, 0, 0, 4, 5, 3, 1, 1, 4, 1]

control = False

sum = 0
counter = 0
multiplier = 7

for i in range(12):
    sum += (emso[i] * multiplier)
    multiplier -= 1
    
    print(sum)
    if i == 5:
        multiplier = 7  

sum += emso[12]

if sum % 11 == 0:
    control = True

if control == True:
    print("EMŠO je veljaven")
else:
    print("EMŠO ni veljaven")
