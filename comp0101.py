class Solution(object):
    def cost(self, s, indx):
        indx1 = 0
        c = s[indx]
        sum_c = 0
        while(indx1<indx):
            if s[indx1]==c:
                sum_c+=1
            indx1+=1
        return sum_c
    def minimizeStringValueAux(self, s,abc):
        curr = abc[0]
        s1 = ""
        for indx1, c in enumerate(s):
            if(c=='?'):
                s1+=curr
                indx = 0
                if(abc.index(curr)+1<len(abc)): indx = abc.index(curr)+1
                curr = abc[indx]
            else:
                s1+=c
                if(abc.index(c)>=abc.index(curr)):
                    indx = 0
                    if(abc.index(c)+1<len(abc)): indx = abc.index(c)+1
                    curr = abc[indx]
        return s1
    def minimizeStringValue(self, s):
        #n = self.cost(i,s)
        return self.minimizeStringValueAux(s,"abcdefghijklmnopqrstuvwxyz")

s = Solution()
print(s.minimizeStringValue("abcdefghijklmnopqrstuvwxy??"))
