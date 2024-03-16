def ri(L, i):
    if i == len(L):
        return [[]]  # Return a list with an empty list if i is the length of L
    subsets = ri(L, i + 1)  # Recursively call r with the next index
    return subsets + [subset + [L[i]] for subset in subsets]

def checkSum(L,k):
    for l in ri(L,0):
        print(l,sum(l))

L=[1,2,3]
ri1 = checkSum(L, 3)
print(ri1)
