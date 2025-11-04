class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        i,j=0,len(s)-1
        while i<j:
            if (s[i] == s[j]):
                i+=1
                j-=1
            else:
                return False
        return True
        