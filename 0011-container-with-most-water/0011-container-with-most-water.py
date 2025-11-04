class Solution(object):
    def maxArea(self, height):
        l=0
        r=len(height)-1
        maxar = 0
        while l<r:
            h = min(height[l],height[r])
            b = (r+1) - (l+1)
            area = h*b
            maxar = max(maxar,area)
            if (height[l]>height[r]):
                r-=1
            elif (height[l]<height[r]):
                l+=1
            else:
                l+=1
        return maxar

        
        