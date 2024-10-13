"""Napiši funkcijo nepadajoc(s), ki za podani seznam pove, ali je nepadajoč, torej,
ali je vsak element enak ali večji od svojega predhodnika."""

seznam = [10, 6, 6, 5, 2, 3]

def nepadajoc(s):
    element = s[0]
    nepadajoc = True
    for i in range(1, len(s)):
        if s[i] <= element:
            element = s[i]
        else:
            nepadajoc = False
    return nepadajoc

if nepadajoc(seznam) == False:
    print("Podani seznam ni padajoč.")
else:
    print("Podani seznam je padajoč.")
