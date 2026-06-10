import math
class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    def minOperations(self, nums, numsDivide):
        g = numsDivide[0]
        for x in numsDivide[1:]:
            g = self.gcd(g,x)
        nums.sort()
        for i in range(len(nums)):
            if g%nums[i] == 0:
                return i
        else:
            return -1
        