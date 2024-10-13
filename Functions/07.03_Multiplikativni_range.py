"""Napiši funkcijo, ki vrne seznam, kjer je vsako naslednje število za podani faktor
večje od prejšnjega. Npr., v seznamu [1,2,4,8,16] je vsako naslednje število dvakrat
večje od prejšnjega. Argumenti funkcije naj bodo začetno število, faktor in dolžina seznama."""

st = int(input("Vnesi celo stevilo: "))
fak = int(input("Vnesi faktor: "))
d_arr = int(input("Vnesi dolzino seznama: "))

def multiplikativni_range(stevilo, faktor, dolzina_tabele):
    arr = []
    st_n = stevilo
    
    for i in range(d_arr):
        arr.append(st_n)
        st_n *= faktor     
    return arr

print(multiplikativni_range(st, fak, d_arr))
