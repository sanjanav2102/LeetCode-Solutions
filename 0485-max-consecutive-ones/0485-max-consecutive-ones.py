class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        i=0
        j=0
        c = 0
        max_val = 0
        n = len(nums)
        while j < n:
            if nums[j] == 1:
                c+=1
                j+=1
            else:
                max_val = max(max_val,c)
                c = 0
                i = j+1
                j+=1
            max_val = max(max_val,c)
        return max_val

        

        