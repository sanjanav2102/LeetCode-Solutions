class Solution(object):
    def floodFill(self, image, sr, sc, color):

        newcolor = image[sr][sc]
        ans = image
        delrow = [-1,0,1,0]
        delcol = [0,1,0,-1]
        n = len(image)
        m = len(image[0])

        def dfs(sr,sc,ans,image,newcolor,delrow,delcol):
            ans[sr][sc] = color

            for i in range(0,4):
                nrow = sr + delrow[i]
                ncol = sc + delcol[i]

                if (nrow>=0 and nrow<n and ncol>=0 and ncol<m and image[nrow][ncol] == newcolor and ans[nrow][ncol] != color):
                    dfs(nrow,ncol,ans,image,newcolor,delrow,delcol)

            return ans

        return dfs(sr,sc,ans,image,newcolor,delrow,delcol)