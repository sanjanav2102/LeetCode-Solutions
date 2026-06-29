class Solution(object):
    def findgcd(self,a,b):
        while b!= 0:
            a,b = b, a%b
        return a 
    def findlcm(self,a,b):
        return (a*b)/self.findgcd(a,b)
    def subarrayLCM(self, nums, k):
        c = 0
        for i in range(len(nums)):
            lcm = 1
            for j in range(i,len(nums)):
                lcm = self.findlcm(lcm,nums[j])
                if lcm == k:
                    c+=1
            
        return c

           

            
       


