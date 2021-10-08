# Python3 program for Naive Pattern
# Searching algorithm


fileName = "fastqFormat.txt"
file = open(fileName, "r")
linecounter=1
txtList = []

while True:
    txt = file.readline().strip()
    if len(txt) == 0:
        file.close()
        break
    print("linecounter%4 is: ", linecounter%4)
    if linecounter%4 == 2:
        txtList.append(txt)
        print("txtList is", txtList)
    print("linecounter is: ",linecounter,"readline as: ", txt)
    linecounter += 1




def search(pat, txt):
    print("Start search")
    M = len(pat)
    print("pat is: ", pat)
    N = len(txt)
    print("txt is: ", txt)
    # A loop to slide pat[] one by one */
    for i in range(N - M + 1):
        j = 0

        # For current index i, check
        # for pattern match */
        while(j < M):
            if (txt[i + j] != pat[j]):
                break
            j += 1

        if (j == M):
            print("Pattern found at index ", i)

# Driver Code
if __name__ == '__main__':

    for i in range(len(txtList)):
        txt = txtList[i]
        pat = "AAAA"
        search(pat, txt)

# This code is developed
# by Tom Stevns 2021
