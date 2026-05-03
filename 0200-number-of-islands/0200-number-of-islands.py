class Solution(object):
    def numIslands(self, grid):
        def bfs(i,j,vis,grid):
            q=[]
            q.append([i,j])
            vis[i][j] = 1
            while q:
                i = q[0][0]
                j = q[0][1]
                q.pop(0)
                #traverse neighbors
                # see image in docs
                #for deli in range (-1,2):
                 #   for delj in range (-1,2):
                  #      ni = i+deli
                   #     nj = j+delj
                for deli, delj in [(-1,0),(1,0),(0,-1),(0,1)]:
                    ni = i + deli
                    nj = j + delj
                    if (ni >=0 and ni < n and nj>=0 and nj<m and grid[ni][nj] == '1' and not vis[ni][nj]):
                        vis[ni][nj] = 1
                        q.append([ni,nj])

        n = len(grid)
        m = len(grid[0])
        c =0
        #vis = [([0]*m)]*n
         # ✅ fix visited matrix
        vis = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if not vis[i][j] and grid[i][j] == '1':
                    c+=1
                    bfs(i,j,vis,grid)
        return c



         
        