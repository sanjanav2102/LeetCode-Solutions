class Solution(object):
    def findGcd(self,a,b):
        while b!= 0:
            a,b = b,a%b
        return a

    def subarrayGCD(self, nums, k):
        c = 0
        for i in range(len(nums)):
            gcd = 0
            for j in range(i,len(nums)):
                gcd = self.findGcd(gcd,nums[j])
                if gcd == k:
                    c+=1
                elif gcd < k:
                    break
        return c