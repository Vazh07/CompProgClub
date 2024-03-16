L = [6,3,4,9,5,7,8]

def ri(L, i):
    if i == len(L):
        return [[]]  # Return a list with an empty list if i is the length of L
    subsets = ri(L, i + 1)  # Recursively call r with the next index
    return subsets + [subset + [L[i]] for subset in subsets]

ri1 = ri(L, 0)
print(ri1)

def r(L,i):
    if(len(L)<i+1): return L
    return r(L,i+1)+[L[i]]+r(L,i+1)


ri = r(L,0)
print(ri)


memo1=[[0 for _ in range(10000)] for _ in range(10000)]#Max Items, Max Cap
def k(c,v,w,i):
    if c < 0: return (1<<32)*-1
    if c == 0: return 0
    if i == len(w): return 0
    if memo1[i][c]: return memo1[i][c]
    memo1[i][c]=max(k(c,v,w,i+1),v[i]+k(c-w[i],v,w,i+1))
    return memo1[i][c]

def knapsack_memoization(c, v, w):
    n = len(v)
    memo = [[None] * (c + 1) for _ in range(n + 1)]
    def knap_helper(capacity, item_index):
        if memo[item_index][capacity] is not None:
            return memo[item_index][capacity]
        if capacity == 0 or item_index == 0:
            memo[item_index][capacity] = 0
            return 0
        if w[item_index - 1] > capacity:
            memo[item_index][capacity] = knap_helper(capacity, item_index - 1)
            return memo[item_index][capacity]
        memo[item_index][capacity] = max(
            knap_helper(capacity, item_index - 1),
            v[item_index - 1] + knap_helper(capacity - w[item_index - 1], item_index - 1)
        )
        return memo[item_index][capacity]
    return knap_helper(c, n)

# Example usage:
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value = knapsack_memoization(capacity, values, weights)
mv1 = k(capacity,values,weights,0)
print("Maximum value that can be obtained:", max_value, '::', mv1)
