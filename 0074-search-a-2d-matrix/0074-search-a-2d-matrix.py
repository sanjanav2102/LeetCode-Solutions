class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        # Step 1: Find the row
        low, high = 0, m - 1
        row = -1

        while low <= high:
            mid = (low + high) // 2

            if matrix[mid][0] <= target <= matrix[mid][n - 1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                low = mid + 1

        if row == -1:
            return False

        # Step 2: Binary search in that row
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False