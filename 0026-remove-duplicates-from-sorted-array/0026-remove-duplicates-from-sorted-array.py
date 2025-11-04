class Solution(object):
    def removeDuplicates(self, nums):
        l = 0
        r = 1
        k=1
        for r in range(0,len(nums)):
            if (nums[l] == nums[r]):
                r+=1
            else:
                nums[l+1] = nums[r]
                k+=1
                l+=1
                r+=1
        return k

        