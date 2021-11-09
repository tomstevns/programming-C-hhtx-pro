"""
I denne afleveringsopgave3 skal du løse 6 opaver udførligt forklaret nedenfor.
Opgaverne stilles med udgangspunkt i de øvelser vi har gennemgået i lektionerne indtil nu

Opgavernes sværhedsgrad  stiger løbende og skal derfor prmært løses med den "Opgave 1" først,
men det er for såvidt op til dig selv, hvilken rækkefølge du vil løse dem i.

Jeg har vedlagt en python fil "Afleveringsopgave3.py" hvor opgaverne skal programmeres ind i.

Du skal gå igang med at løse opgaverne i den kommende uge41's lektioner,
hvor vi allesammen skal hjælpe hinanden med at nå så godt i mål som muligt :o)

Held og lykke !
Tom

Du bliver bedømt efter 7 trins skalalen og stepper et karaktertrin op for
hver korrekt løst opgave som følger:

Ingen aflevering:       -03
Opgave 1 løst korrekt:  0
Opgave 2 løst korrekt:  2
Opgave 3 løst korrekt:  4
Opgave 4 løst korrekt:  7
Opgave 5 løst korrekt:  10
Opgave 6 løst korrekt:  12

Generelt for samtlige opgaver gælder at de SKAL løses ved at bruge funktioer.
Et eksempel på en funktion er vist nedenfor som returnerer værdien 10

def visTal():
    return 10


Du placerer dine løsninger der hvor det står angivet nedenfor.
Måske er Opgave 1 allerede lavet!!!!!!

"""


"""Opgave 1:
- lav en funktion som hedder beregnModulus(heltal,modulusværdi)
- funktionen skal gøre følgende
    - beregn modulus ud fra heltal og modulusværdi og m
    - print resultat
    -returner resulat
    
unit-test funktion med følgende kode:


beregnModulus(11,2)
beregnModulus(10,2)
beregnModulus(11.5,2)
beregnModulus(10,2.0)
beregnModulus(10,2.1)




"""

#funktionen ganger et tal med syv og returnerer resultatet
def gangTalMed7(inputTal):
    #printer input
    print("input tal er: ", inputTal)
    #ganger input med 7
    resultat = inputTal*7
    #printer resultat
    print("resultat er: ", resultat)
    #funktionen gangTalMed7() returnerer resultat
    return resultat

#test funtion med input tal 10
gangTalMed7(10)

"""Opgave 2:
- lav en funktion som hedder lægToTalSammen 
- funktionen skal gøre følgende
    - print input tallene
    - læg tallene sammen
    - print resultat
    -returner resulat
    
test funktion med følgende kode:

lægToTalSammen(10,7)
"""

#funktionen adderer to tal og returnerer resultatet
def lægToTalSammen(inputTal1,inputTal2):
    print("input tal1 er: ", inputTal1)
    print("input tal2 er: ", inputTal2)
    # Lav resten selv

#lægToTalSammen()


"""Opgave 3:
- lav en funktion som hedder lægToStrengeSammen 
- funktionen skal gøre følgende
    - print input strengene
    - læg strengene sammen
    - print resultat
    -returner resulat
    
test funktion med følgende kode:

lægToStrengeSammen("Vi har efterårsferie i uge","42")
"""

#funktionen adderer to strenge og returnerer resultatet
def lægToStrengeSammen(inputStreng1,inputStreng2):
    # Lav resten selv
    print("")

lægToStrengeSammen("a","b")

"""Opgave 4:
- lav en funktion som hedder talletErStørreEndTI 
- funktionen skal gøre følgende
    - print input tal
    - lav en IF sætning som sætter resultat til True hvis tallet er større end 10
    - lav en Else sætning som sætter resultat til False hvis tallet er mindre end 10
    - print resultat
    -returner resulat
    
test funktion med følgende kode:

talletErStørreEndTI(11)
talletErStørreEndTI(10)
talletErStørreEndTI(9)
talletErStørreEndTI(-11)
"""


def talletErStørreEndTI(dummy):
    # Lav resten selv
    print("")

#tester funktionen med følgende kode:

talletErStørreEndTI(23423)
    # Lav resten selv



"""Opgave 5:
- lav en funktion som hedder printInputværdiFraInputVærdiTilNul  
- funktionen skal gøre følgende
    
    - print inputværdi
    - resultat = resultat + inputværdi
    - print inputværdi-1
    - resultat = resultat + inputværdi
    - print inputværdi-2
    - resultat = resultat + inputværdi
    etc.......
    - print inputværdi - inputværdi
    - resultat = resultat + inputværdi
    -returner resulat
    
test funktion med følgende kode:

printInputværdiFraInputVærdiTilNul(10)
"""

# Opgave 5 laves her


"""Opgave 6:
- lav en funktion som hedder getValutasKurs  
- funktionen skal gøre følgende
    - kunne håndtere at returnere valutakursen for følgende valutakoder
      JPY, RAN , DKK, EUR, GBP
    - kunne håndtere at returnere en fejl besked for valutakoder som funktionen ikke kender på forhånd
    - print inputværdi
    - resultat = valutakodens tilhørende kursværdi 
    - print resultat
    -returner resulat
    
test funktion med følgende kode med inputværdierne: JPY, RAN , DKK, EUR, GBP, NOK, USD
"""

# Opgave 6 laves her


