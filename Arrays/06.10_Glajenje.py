"""Napišite program, ki izračuna tekoče poprečje danega zaporedja. Seznam števil naj bo v
programu dan, kot rezultat naj program izpiše seznam povprečij štirih zaporednih
elementov.
Tekoče poprečje seznama [3, 5, 8, 0, 7, -3, 12, 0, -5, 5] je [4, 5, 3,
4, 4, 1, 3]: poprečje elementov 3, 5, 8, 0 je 4, poprečje 5, 8, 0, 7 je 5, poprečje 8, 0,
7, -­‐3 je 3 ..."""

array = [3, 5, 8, 0, 7, -3, 12, 0, -5, 5]
avg_array = []

sum = 0

for i in range(len(array)-3):
    for j in range(4):
        sum += array[i]
        #print(sum)
        i += 1
    avg = sum / 4
    avg_array.append(avg) 
    sum = 0

print(avg_array)
