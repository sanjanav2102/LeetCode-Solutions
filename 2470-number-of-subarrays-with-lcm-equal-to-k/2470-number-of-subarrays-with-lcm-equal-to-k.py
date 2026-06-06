
class Solution(object):
    def findGcd(self,a,b):
        while b!=0 :
            a,b = b,a%b
        return a 
    def findLcm(self,a,b):
        return (a*b)//self.findGcd(a,b)
    def subarrayLCM(self, nums, k):
        c = 0
        for i in range(len(nums)):
            lcm = 1 #minimum reset value 1
            for j in range(i,len(nums)):
                lcm = self.findLcm(lcm,nums[j])
                if lcm == k:
                    c+=1
                elif lcm>k:
                    break
        return c
    
        
        