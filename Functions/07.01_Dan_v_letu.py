"""Napiši funkcijo dan_v_letu(dan, mesec), ki prejme datum v letu 2024 in vrne zaporedno
številko dneva v letu. Tako je, na primer, 10. februar 41. dan v letu. Leto 2024 je seveda prestopno."""

dan = int(input("Vnesi dan: "))
mesec = int(input("Vnesi mesec: "))


def dan_v_letu(dan, mesec):
    leto = [31, 29, 31, 30, 30, 31, 31, 30, 31, 30, 31]
    st_dneva = 0

    for i in range(mesec - 1):
        st_dneva += leto[i]
    st_dneva += dan
    return st_dneva

d = dan_v_letu(dan, mesec)
print(str(dan) + ".", str(mesec) + ".", "je", str(d) + ". dan v letu 2024.")
