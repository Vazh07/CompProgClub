def knap(cap, items,i):
    if(i==0): return 0
    if(cap==0):return 0
    if(cap<0): return (1<<60)*-1
    return max(knap(cap,items,i-1),
        items[i][0]+knap(cap-items[i][1],items,i-1))

print(knap(100,[[5,7],[7,5],[10,8],[25,15],[50,100],[40,30]],5))
