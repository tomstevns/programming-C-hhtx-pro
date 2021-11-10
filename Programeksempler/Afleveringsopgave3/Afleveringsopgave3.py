"""
I denne afleveringsopgave3 skal du løse 6 opaver udførligt forklaret nedenfor.
Opgaverne stilles med udgangspunkt i de øvelser vi har gennemgået i lektionerne indtil nu

Opgavernes sværhedsgrad  stiger løbende og skal derfor primært løses med den "Opgave 1" først,
men det er for såvidt op til dig selv, hvilken rækkefølge du vil løse dem i.

Jeg har vedlagt en python fil "Afleveringsopgave3.py" hvor opgaverne skal programmeres ind i.

Du skal gå igang med at løse opgaverne i den kommende uge45+46's lektioner,
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

"""


"""Opgave 1:
- lav en funktion som hedder beregnModulus(heltal,modulusværdi)
- funktionen skal gøre følgende
    - beregn modulus ud fra heltal og modulusværdi
    - print resultat
    -returner resulat
    
unit-test funktion med følgende kode:

beregnModulus(11,2)
beregnModulus(10,2)
beregnModulus(11.5,2)
beregnModulus(10,2.0)
beregnModulus(10,2.1)
"""


"""Opgave 2:
- lav en funktion som heddder findAntalKromosomerIFil(filnavn) 
- funktionen skal gøre følgende
    - finde antal af karakteren > i filen
    - print dette antal
    -returner antal 
    
Du kan finde inspiration til at løse opgaven i den vedlagte fil
naivePatternSearchingFromFastqFile.py. Både hvad angår det at håndtere
en fil med at åbne læse og lukke den, såvel som at søge efter karakterer, som
i dette tilfælde er karakteren >

test funktion med følgende kode:

#teste funktion med filen opgave2.fasta
findAntalKromosomerIFil(opgave2.fasta)
#teste funktion med et filnavn som ikke eksisterer
findAntalKromosomerIFil(etFilnavnSomIkkeEksisterer)
"""

"""Opgave 3:
- tilføj kode til funktionen som heddder findAntalKromosomerIFil(filnavn) - dvs opgave2 
- Funktionen skal kunne håndterer en situation hvor noget går galt nåt man åbner
læser eller lukker filen 
    
Du kan finde inspiration til at løse opgaven i den vedlagte fil
naivePatternSearchingFromFastqFile.py. Både hvad angår det at håndtere
en fil med at åbne læse og lukke den, såvel som at søge efter karakterer, som
i dette tilfælde er karakteren >

test funktion med følgende kode:

#teste funktion med filen opgave2.fasta
findAntalKromosomerIFil(opgave2.fasta)
#teste funktion med et filnavn som ikke eksisterer
findAntalKromosomerIFil(etFilnavnSomIkkeEksisterer)
"""


"""Opgave 4:
- lav en funktion som hedder findAntalStartCodonATGIFil(filnavn) 
- funktionen skal gøre følgende
    - finde antallet af de 3 karakterer "ATG"  i filen
    - print dette antallet
    -returner antal 

test funktion med følgende kode:

#teste funktion med filen opgave2.fasta
findAntalStartCodonATGIFil(opgave2.fasta)
"""

"""Opgave 5:
- lav en funktion som heddder findAntalCodonIFil(inputCodon,filnavn) 
- funktionen skal gøre følgende
    - finde antallet af de 3 karakterer som er beskrevet i inputCodon  
    - print dette antallet
    -returner antal 

test funktion med følgende kode:

#teste funktion med filen opgave2.fasta

findAntalCodonIFil("TGA",opgave2.fasta) #Start Codon
findAntalCodonIFil("TAG",opgave2.fasta) #Stop  Codon
findAntalCodonIFil("TAA",opgave2.fasta) #Stop  Codon
findAntalCodonIFil("TGA",opgave2.fasta) #Stop  Codon
"""

"""Opgave 6:
- lav en funktion som heddder findforskelMellemStartogStopCodens(filnavn) 
- funktionen skal gøre følgende
    StartCodons: Finde antallet af start codons(ATG) og printe værdien
    StopCodons: Finde det samlede antal af stop codons(TAG+TGA+TAA) og printe værdien
    Finde differencen mellem antallet af start og stop codons
    -returner differencen

test funktion med følgende kode:

#teste funktion med filen opgave2.fasta

# test om nedenstående funktion returnerer 0 eller forskellig fra 0
findforskelMellemStartogStopCodens(opgave2.fasta) 
"""
