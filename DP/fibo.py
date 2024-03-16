dp = [0]*1000
dp[0] = 1
dp[1] = 1
def fib(n):
    if dp[n]:
        print("Memo")
        return dp[n]
    dp[n]=fib(n-1)+fib(n-2)
    print(n,[i for i in dp if i])
    return dp[n]

print(fib(10))
