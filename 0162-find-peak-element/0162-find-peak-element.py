class Solution(object):
    def findPeakElement(self, nums):
        l = 0
        for h in range(1,len(nums)):
            if nums[h-1] <= nums[h]:
               # l+=1
               h+=1
               if h == len(nums):
                return h-1
                
            else:
                return h-1
        else:
            return 0

        