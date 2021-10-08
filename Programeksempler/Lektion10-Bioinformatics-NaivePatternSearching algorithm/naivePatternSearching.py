# Python3 program for Naive Pattern
# Searching algorithm

file = open("fastqFormat.txt", "r")
print(file.readline())



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
    txt = "CTGGGACCTAGCGCGCTAGAGATCGAAGGATCATAGCGTAGXCTAAAAAAGGTCGAGAGAGGTACTAGGTCGAAGCG"
    pat = "TCGA"
    search(pat, txt)

# This code is developed
# by Tom Stevns 2021
