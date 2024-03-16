class Solution(object):
    def coinMtrx(self, coins, amount, dp, indx):
        if amount==0:
            for indx2, opt in enumerate(dp):
                print(f"Coin {indx2+1}:",opt)
            return
        for indx1, coin in enumerate(coins):
            if amount%coin==0:
                dp[indx1].append(amount/coin)
            else: dp[indx1].append(1<<32)
        self.coinMtrx(coins, amount-1, dp, indx)
    def changeDp(self, coins, amount, dp, indx):
        if amount == 0: return 0
        if amout < 0: return -1
        for coin in coins:
            self.changeDp(coins, amount-coin, dp, indx)
    def coinChange(self, coins, amount):
        if amount == 0: return 0
        dp=[[] for _ in coins]
        return self.changeDp(coins,amount,dp, 0)

s = Solution()
for i in range(5,10+1):
    print(f"Amount {i}:",s.coinChange([1,2,5],i))
