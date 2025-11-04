class Solution:
    def moveZeroes(self, nums):
        e = len(nums)
        l,r=0,0
        for i in range(0,e):
            if nums[i] != 0:
                nums[l],nums[i] = nums[i],nums[l]
                l+=1
            
        
