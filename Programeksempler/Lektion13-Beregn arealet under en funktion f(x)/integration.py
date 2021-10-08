# f = 3x

def integration(f,n,l,p,pr): # Variablerne er funktionskonstanten, opløsningen (n), øvre grænse (l), potens, hvorvidt mellemregninger skal printes.
    areal = 0

    for i in range(n*l):
        interval = 1/n
        x = i / n
        y = f * pow(x,p)
        a = y * interval

        areal = areal + a
        if pr == 1:
            print(a)

    print(areal)

f = int(input("Indtast konstant "))
n = int(input("Indtast opløsning "))
l = int(input("Indtast ydre grænse "))
p = int(input("Indtast potens "))
pr = int(input("Vil du have mellemregninger printet? 1 for Ja, 0 for Nej "))

integration(f,n,l,p,pr)
