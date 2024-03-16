def arrayQuery(arr,queries):
    print("ArrayQueries:",arr,queries)
    marked = [n for n in arr]
    s = []
    for q in queries:
        for indx1, i in enumerate(arr):
            if(indx1==q[0]):
                print(indx1,q[0])
                marked[indx1]=False
                men = q[1]
                while(men):
                    mins=[i23 for i23 in marked if i23]
                    if mins: marked[marked.index(min(mins))]=False
                    men=men-1
                break
        #s.append(sum([i24 for i24 in marked if i24]))
    return s

print(arrayQuery([1,2,2,1,2,3,1],[[1,2],[3,3],[4,2]]))
print("///////////////////////////////////////////////////////////////////////////////////")
print(arrayQuery([1,4,2,3], [[0,1]]))
