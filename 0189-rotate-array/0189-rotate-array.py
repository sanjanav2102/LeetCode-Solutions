class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k%n
        if k == 0:
            return nums
        temp =  [0]*k
        for i in range(k):
            temp[i] = nums[n-k+i]
        for i in range(n-k-1,-1,-1):
            nums[i+k] = nums[i]
        for i in range(len(temp)):
            nums[i] = temp[i]
        return nums

            
        