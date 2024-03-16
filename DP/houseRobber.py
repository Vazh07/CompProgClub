class Solution(object):
    def rob(self, nums):
        dp=[-1 for _ in nums]
        for indx1, num1 in enumerate(nums):
            max_n = nums[indx1]
            for indx2, num2 in enumerate(nums):
                if(indx1!=indx2 and indx2!=indx1+1 and indx2!=indx1-1):
                    s = nums[indx1]+nums[indx2]
                    if(s>max_n):
                        max_n=s
                        dp[indx2]=max_n
                        print(dp)
            dp[indx1]=max_n
        return dp[-1]
s = Solution()
print(s.rob([1,2,3,1]))
