class Solution(object):
    def orangesRotting(self, grid):
        n = len(grid)
        m = len(grid[0])
        max_time = 0
        time = 0
        q = []
        vis = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if (grid[i][j] == 2 ):
                    q.append([[i,j],0])
                    vis[i][j] = 1
                else:
                    vis[i][j] = 0

        dr = [-1,+0,+1,+0]
        dc = [+0,+1,+0,-1]
        while len(q) != 0:
            node = q.pop(0)
            r = node[0][0]
            c = node[0][1]
            time = node[1]
            max_time = max(max_time,time)
            for i in range(4):
                nr = r+dr[i]
                nc = c+dc[i]
                if (nr>=0 and nr<n and nc>=0 and nc<m and vis[nr][nc] ==0 and grid[nr][nc] == 1):
                    q.append([[nr,nc],time+1])
                    vis[nr][nc] = 1
        for i in range(n):
            for j in range(m):
                if (vis[i][j] == 0 and grid[i][j] == 1 ):
                    return -1
     
        return max_time







