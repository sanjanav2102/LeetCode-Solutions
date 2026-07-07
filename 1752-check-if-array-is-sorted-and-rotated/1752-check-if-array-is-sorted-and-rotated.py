class Solution(object):
    def is_sorted(self,r):
        for i in range(1,len(r)):
            if r[i-1]>r[i]:
                return False
        return True

    def check(self, nums):
        for k in range(len(nums)):
            rotated_array = nums[k:]+nums[:k]
            ans = self.is_sorted(rotated_array)
            if ans == True:
                return True
        else: 
            return False
