class Solution(object):
    def merge(self,a,left,right):
        i,j,k = 0,0,0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                a[k] = left[i]
                i+=1
            else:
                a[k] = right[j]
                j+=1
            k+=1
        while i<len(left):
            a[k] = left[i]
            i+=1
            k+=1
        while j<len(right):
            a[k] = right[j]
            j+=1
            k+=1
    def merge_sort(self,a):
        if len(a)>1:
            mid=len(a)//2
            left = a[:mid]
            right = a[mid:]

            self.merge_sort(left)
            self.merge_sort(right)

            self.merge(a,left,right)
        
        


    def sortArray(self, nums):
        self.merge_sort(nums)
        return nums
        
   




