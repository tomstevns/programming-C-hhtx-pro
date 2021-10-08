"""
I bunden af pyCharm står der "Python Packages"
klik der og indtast matplotlib.
Herefter skal i trykke på knappen "Install" for at installere og anvende
pakken i pyCharm IDE'et
"""

import matplotlib.pyplot as plt

#Grid plot configuration
w = 4
h = 3
d = 70

print("Nu skal du til at indtaste x og y koordinater i spillet\n*******  SÆNK SLAGSKIBE  *******\n\n")

"""
Her skal du selv tilrette koden i def plotSkudkoordinat(skud)
så du får de aktuelle skudkordinater plottet ud
"""
def plotSkudkoordinat(skud):
    plt.figure(figsize=(w, h), dpi=d)
    plt.axis([0, 5, 0, 5])
    x = [1, 2, 4]
    y = [1, 3, 3]
    size = 500
    plt.scatter(x, y, s=size)
    plt.savefig("out.png")




for x in range(5):

    print("Skud nummer: ",(x+1),"Antal skud tilbage", 5-(x+1))
    xKoordinat = input("Indtast x koordinat ")
    yKoordinat = input("Indtast y koordinat ")
    skudKoordinater = [xKoordinat, yKoordinat]

    # Lektie hvordan kan man lave denne if sætning enklere
    if (((int(skudKoordinater[0]) > 0) and (int(skudKoordinater[0]) < 11)) and ((int(skudKoordinater[1]) > 0) and (int(skudKoordinater[1]) < 11))) :
     print("valide skudkoordinater er: ", skudKoordinater,"\n")
     plotSkudkoordinat(skudKoordinater)
    else:
        print("invalide skudkoordinater prøv igen: ", skudKoordinater,"\n")
