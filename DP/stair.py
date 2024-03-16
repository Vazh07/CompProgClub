class Solution(object):
    def climbDp(self,n,dp):
        if(n==0):return 0
        if dp[n]: return dp[n]
        dp[n]=self.climbDp(n-1,dp)+self.climbDp(n-2,dp)
        return dp[n]

    def climbStairs(self, n):
        dp = [0]*1000
        dp[1]=1
        dp[2]=2
        return self.climbDp(n,dp)


s = Solution()
for i in range(1,5+1):
    print(f"Ways to climb {i}:",s.climbStairs(i))
