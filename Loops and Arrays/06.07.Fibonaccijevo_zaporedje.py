"""Fibonaccijevo zaporedje se začne s številoma 1, 1, vsak naslednji člen pa dobimo tako, da seštejemo prejšnja dva.
1 in 1 je 2, 1 in 2 je 3, 2 in 3 je 5, 3 in 5 je 8 in tako naprej. Zaporedje se tako začne z 1 1 2 3 5 8 13 21 34 55.
Napiši program, ki izpiše prvih 20 členov zaporedja."""

a = 0
b = 1
print(b)

for i in range(19):
    c = a + b
    print(c)
    a = b
    b = c
