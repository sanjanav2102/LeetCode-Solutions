class Solution(object):
    def judgeSquareSum(self, c):
        limit = int(c**0.5)

        for i in range(limit + 1):
            remaining = c - i*i
            root = int(remaining**0.5)

            if root * root == remaining:
                return True

        return False