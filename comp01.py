class Solution(object):
    def encrypt(self,nums):
        max = -1
        s = ""
        for n in str(nums):
            if(int(n)>max):
                max=int(n)
                s = n*len(str(nums))
        return int(s)
    def sumOfEncryptedInt(self, nums):
        max = -1
        s = 0
        for n in nums:
            s+=self.encrypt(n)
        return s

class Solution1(object):
    def getMin(self,nums,marked):
        l = []
        nm = min(nums)
        inm = nums.index(nm)
        if [inm,nm] not in marked: return [inm,nm]
        min_n = 1<<32
        for indx1, num in enumerate(nums):
            if num<min_n: min_n = num
            if [indx1,min_n] not in marked:
                return [indx1, min_n]
        return l
    def unmarkedSumArray(self, nums, queries):
        marked = []
        for q in queries:
            for indx1, i in enumerate(nums):
                if(indx1==q[0]): marked.append([indx1,i])
                men = q[1]
                while men>0:
                    marked.append(self.getMin(nums,marked))
                    men=men-1
            print(marked)

s = Solution1()
print(s.unmarkedSumArray([1,2,2,1,2,3,1],
[[1,2],[3,3],[4,2]]))
