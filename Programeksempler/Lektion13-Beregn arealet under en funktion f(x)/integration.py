

def integration(konstant,resolution,upperBorderValue,p,pr): # Variablerne er konstant, opløsningen (resolution), øvre grænse (upperBorderValue), potens, hvorvidt mellemregninger skal printes.
    areal = 0
    numberOfRangeCount = (resolution*upperBorderValue)
    print("numberOfRangeCount is: ",numberOfRangeCount)
 #   for i in range(numberOfRangeCount):
    for i in range(numberOfRangeCount):

        interval = 1/resolution
#        x = i / resolution
        x = (i+1) / resolution
        y = konstant * pow(x,p)
        a = y * interval

        areal = areal + a
        if pr == 1:
            print("Summeret areal for i= ",i," X=",x," er: ",a)

    print(areal)

konstant = int(input("Indtast konstant som du ganger f(x) med: "))
resolution = int(input("Indtast opløsning: "))
upperBorderValue = int(input("Indtast ydre grænse: "))
p = int(input("Indtast potens: "))
pr = int(input("Vil du have mellemregninger printet? \n1 for Ja, 0 for Nej "))

integration(konstant, resolution, upperBorderValue, p, pr)
