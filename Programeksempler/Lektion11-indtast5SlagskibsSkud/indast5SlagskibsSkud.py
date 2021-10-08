
print("Nu skal du til at indtaste x og y koordinater i spillet\n*******  SÆNK SLAGSKIBE  *******\n\n")

for x in range(5):

    print("Skud nummer: ",(x+1),"Antal skud tilbage", 5-(x+1))
    xKoordinat = int(input("Indtast x koordinat "))
    yKoordinat = int(input("Indtast y koordinat "))
    skudKoordinater = [xKoordinat, yKoordinat]

    # Lektie hvordan kan man lave denne if sætning enklere
 #if (((int(skudKoordinater[0]) > 0) and (int(skudKoordinater[0]) < 11)) and ((int(skudKoordinater[1]) > 0) and (int(skudKoordinater[1]) < 11))) :
 #    print("valide skudkoordinater er: ", skudKoordinater,"\n")
#
 #   else:
  #      print("invalide skudkoordinater prøv igen: ", skudKoordinater,"\n")
