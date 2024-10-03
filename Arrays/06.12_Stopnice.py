"""Stopnišča z neenakimi višinami stopnic lahko opišemo tako, da navedemo višine stopnic,
merjene od tal (ne od prejšnje stopnice). Po stopnicah, opisanih s takšnim seznamom, pleza
robot, ki lahko stopi največ 20 cm visoko. Napišite program, ki za podano tabelo višin stopnic,
izpiše, kako visoko bo robot priplezal.
robot1 = [10, 20, 25, 45, 50, 71, 98, 100]                           5
robot2 = [30, 40,50]                                                 0
robot = [10, 20, 30, 40,45])                                         45
V prvem primeru bo robot pripleza do višine 50, nato pa se ustavi, ker je naslednja stopnica 21
cm višja od te, na kateri stoji. V drugem se ne more povzpeti niti na prvo stopnico. V zadnjem
pripleza do vrha."""

stopnice = [5, 10, 25, 35, 50, 60, 81, 90]
prehojene_stopnice = 0
if stopnice[0] <= 20:
    prehojene_stopnice += 1

    for i in range(len(stopnice)-1):
        if stopnice[i+1] - stopnice[i] <= 20:
            prehojene_stopnice += 1
        else:
            break

print(f"Robot je stopil na {prehojene_stopnice} stopnic.")
