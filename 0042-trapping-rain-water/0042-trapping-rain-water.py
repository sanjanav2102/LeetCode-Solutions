class Solution(object):
    def trap(self, height):
        l=1
        r=len(height)-1
        e=len(height)
        j=1
        l_max=[height[0]]
        r_max=[height[e-1]]
        ans = [0]*len(height)
        for l in range(1,e):
            a = max(l_max[l-1],height[l])
            l_max.append(a)
        for r in range(e-2,-1,-1):
            r_max.append(max(r_max[-1], height[r]))
        r_max.reverse()
        for i in range(0,len(height)):
            ans[i] = min(l_max[i], r_max[i]) - height[i]
        return sum(ans)


            
