class Solution(object):
    def numIslands(self, grid):
        row = len(grid)
        col = len(grid[0])
        no = 0
        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=col or grid[r][c] == '0':
                return 
            grid[r][c] = '0' #visited
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    dfs(i,j)
                    no+=1
        return no
