class Solution(object):
    def isPalindrome(self, s):
        l = 0
        r = len(s)-1
        while l<r:
            if s[l].lower() == s[r].lower():
                l+=1
                r-=1
            elif (s[l].isalnum() == False):
                l+=1
            elif (s[r].isalnum() == False):
                r-=1
            else:
                return False
        return True

        