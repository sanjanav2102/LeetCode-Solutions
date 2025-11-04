class Solution(object):
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            # Calculate area
            width = r - l
            area = min(height[l], height[r]) * width
            max_area = max(max_area, area)

            # Move the pointer at the shorter line
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
