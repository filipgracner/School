"""Napišite program, ki prebere dolžine stranic trikotnika in ugotovi, ali tak trikotnik obstaja."""

a = int(input("Vpisi dolzino stranice a:"))
b = int(input("Vpisi dolzino stranice b:"))
c = int(input("Vpisi dolzino stranice c:"))

if a + b > c and a+c > b and b+c > a:
    print("Trikotnik obstaja.")
else:
    print("Trikotnik ne obstaja.")
