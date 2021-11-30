#Opgave 1
#Lav et program som returnerer længden af en streng

def findLængdeAfStreng(inputStreng):
    strengLængde = len(inputStreng)
    return strengLængde
#Test af opgave1
testStreng = "abcdef340958304g"
print("længden af strengen ",testStreng," er ", findLængdeAfStreng(testStreng)," karakterer")
print("længden af strengen ", testStreng," er ",findLængdeAfStreng(testStreng), " karakterer")


#Opgave2
#Lav et program åbner en fil1, skriver "hej med dig" i filen 13153 gange, men den
# 5.158 gang skrives der "farvel med dig"

#Definer og åben en fil
f = open("fil1", "w")

#Lav et loop 13153 gange som skriver
for i in range(13):
    #IF I er 5158 så
    print("I skal nu være 5158")
    #Skrive i filen - "Farvel med dig"
    #Noget med
    f.write("truttelut")
    #ELSE
    #Skrive i filen - "Hej med dig"
    #Noget med
    f.write("vuffelivuf")

#Luk filen fil1



#Opgave3
#Lav et program åbner en fil1,
#Finder rækken hvor der står "farvel med dig" og returnerer række nummeret på rækken


#Opgave4
#Lav et program som kan udskrive et alfabet ud fra A->Z, ved hjælp af ASCII decimal værdier,
# lidt om ASCII konverteringer her  "fra ASCII tal til en karakter i alfabetet"
# https://stackoverflow.com/questions/4387138/pythonascii-character-decimal-representation-conversion

# som er tæller i et "While Loop" til ret så du udskriver karakterer fra A->Z

for ascii in range(150):
    #hvis ascii > x , dvs x+1 som svarer til karakteren YYY
    #du skl begynd at printe et alfabet ud fra A->Z
    #START med at lave en IF sætning
    if ascii > 65:
        print("ascii decimal tal ", ascii, " til: ", "Indsæt kode her som koverterer Decimal/Karakterer")
    if ascii ==110:
        break

"""
Opgave5: 
Opret en liste ved at vælge et ulige indekselement fra den første liste 
og lige indekselementer fra den anden.
Givet to lister, l1 og l2, 
skriv et program til at oprette en tredje liste l3,
ved at vælge et ulige indekselement fra listen l1 og lige indekselementer fra listen l2.

Givet:

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

Forventet løsning:
Element på ulige indekspositioner fra liste et
[6, 12, 18]
Element ved lige indekspositioner fra liste to
[4, 12, 20, 28]

Udskrivning Endelig tredje liste
[6, 12, 18, 4, 12, 20, 28]





"""
