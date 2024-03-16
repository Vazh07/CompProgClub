def multiply(a,b):
    r = int(a)*int(b)
    numsA = []
    numsB = []
    for num1 in a:
        numsA.append(num1)
    for num2 in b:
        numsB.append(num2)
    for numA in numsA:
        for numB in numsB:
            print(numA,numB)

multiply('345','56')
