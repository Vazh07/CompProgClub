def quick(arr,flag):
    if len(arr) <= 1:
        print(arr,flag)
        return arr
    pivot = arr[len(arr) // 2]
    print(arr,pivot,flag)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick(left,"L") + middle + quick(right,"R")

quick([7,10,6,9,8,1,2],"r")
