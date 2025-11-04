class Solution:
    def moveZeroes(self, nums):
        temp=[]
        z = 0
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                temp.append(nums[i])
            else:
                z+=1
        nz = len(temp)
        for i in range(0,nz):
            nums[i] = temp[i]
        for i in range(n-z,n):
            nums[i]= 0
