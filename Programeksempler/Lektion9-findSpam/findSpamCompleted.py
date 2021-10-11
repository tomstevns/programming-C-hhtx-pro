spamWords = ["køb","tilbud", "vundet", "tillykke"]   # Create new list
print("Søg efter følgedende angivne spamwords \n",spamWords)
spamWords.append("spam")
testMail1 = "Dette er et tilbud fra Lars Larsen "
testMail2 = "Dette er en testmaill hvor du har vundet 500 kr - tillykke"
#lav teststreng med inputfil eller index af mange filer
spamwordsfound = 0
for i in range(len(spamWords)):
 if spamWords[i] in testMail1:
  print("Spamword ", spamWords[i], "in testMail1 is: ", spamWords[i] in testMail1)
  spamwordsfound += 1
print("spam words found = ",spamwordsfound)
spamwordsfound = 0

#initier spawords og nulstil
spamwordsfound = 0
for i in range(len(spamWords)):
 if spamWords[i] in testMail2:
  print("Spamword ", spamWords[i], "in testmail2 is: ", spamWords[i] in testMail2)
  spamwordsfound += 1
print("spam words found = ",spamwordsfound)
