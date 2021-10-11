
spamWords = ["køb","tilbud", "vundet", "tillykke"]   # Create new list
print(spamWords)
spamWords.append("spam")
"""
print(spamWords)

print("len(spamWords) is:", len(spamWords))
for p in range(len(spamWords)):
 print("Poppet element er: ", spamWords.pop(), "resterende elementer listen", spamWords)


#print("spamWords efter pops",spamWords)
"""



testMail1 = "Dette er en testmail "
testMail2 = "Dette er en testmaill hvor du har vundet 500 kr - tillykke"
#lav teststreng med inputfil eller index af mange filer

spamwordsfound = 0

for i in range(len(spamWords)):
 if spamWords[i] in testMail1:
  print("Spamword ", spamWords[i], "in spamlist is: ", spamWords[i] in testMail1)
  spamwordsfound += 1

print("spam words found = ",spamwordsfound)
#initier spawords og nulstil
spamwordsfound = 0

for i in range(len(spamWords)):
 if spamWords[i] in testMail2:
  print("Spamword ", spamWords[i], "in spamlist is: ", spamWords[i] in testMail2)
  spamwordsfound += 1
print("spam words found = ",spamwordsfound)
