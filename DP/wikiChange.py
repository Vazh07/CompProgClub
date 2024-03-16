class Solution(object):
    def _get_change_making_matrix(self,set_of_coins, r):
        m = [[0 for _ in range(r + 1)] for _ in range(len(set_of_coins) + 1)]
        for i in range(1, r + 1):
            m[0][i] = float('inf')
        return m
    def coinChange(self, coins, n):
        m = self._get_change_making_matrix(coins, n)
        for c, coin in enumerate(coins, 1):
            for r in range(1, n + 1):
                if coin == r:
                    m[c][r] = 1
                elif coin > r:
                    m[c][r] = m[c - 1][r]
                else:
                    m[c][r] = min(m[c - 1][r], 1 + m[c][r - coin])
                print(m)
        return -1 if m[-1][-1] == float('inf') else m[-1][-1]


s = Solution()
for i in range(5,10+1):
    print(f"Amount {i}:",s.coinChange([1,2,5],i))
