class Solution(object):
    def findMedianSortedArrays(self, L1, L2):
        L3=L1+L2
        m=len(L1)
        n=len(L2)
        L3.sort()
        p=m+n
        if p%2==0:
            n1=(L3[p//2 - 1] + L3[p//2]) / 2.0
            return n1
        else:
            k = p//2
            n1=L3[k]
            return n1
        
        