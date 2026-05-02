class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        # Initialize adjacency list
        adj = defaultdict(list)
        #convert the adjacency matrix into alist
        V = len(isConnected)
        vis = [False]*V
        prov = 0
        for i in range(V):
            for j in range(V):
                if isConnected[i][j] == 1 and i != j:
                    adj[i].append(j)
        def dfs(node, vis,adj):
            vis[node] = True
            for i in adj[node]:
                if not vis[i]:
                    dfs(i,vis,adj)
        for i in range(V):
            if not vis[i]:
                prov+=1 
                dfs(i,vis,adj)
        return prov

            

      


         

               
        
