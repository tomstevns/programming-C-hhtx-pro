#Starter med at skrive hvilken valuta man ønsker at konvertere til
#V og viser hvilke valgmuligheder man har ved at printe et dictionary
# Opret et dictionary over valuta:kurs,.....
valutaer = {"EUR":7.46,"USD":6.79,"AUD":4.5,"GBP":8.31,"SEK":0.71,"NOK":0.69}
print("hvilken valuta  ønsker du at konvertere til",valutaer.keys())
konverterValutaTil = (input("Hello user, which currency do You want to convert to?\n"))
konverterValutaTil=konverterValutaTil.upper()
#Vis Valutakursen for du ønsker at konvertere til
print("Valutakursen for ",konverterValutaTil," er: ",valutaer.get(konverterValutaTil))
#Indtast det beløb du ønsker at få konverteret
DKK = float(input("Hello user, how many DKK du you want to convert?\n"))
#Print det beløb som du skal have efter konvertering dvs "antal danske kroner"*"ønsket valuta kurs"


print("You got ",DKK/valutaer.get(konverterValutaTil)," in ",konverterValutaTil )
