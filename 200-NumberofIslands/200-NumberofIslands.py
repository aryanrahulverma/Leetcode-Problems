# Last updated: 12/5/2025, 6:49:25 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        cnt = 0
4        n, m = len(grid), len(grid[0])
5
6        def dfs(i, j):
7            if i < 0 or j < 0 or i >= n or j >=m or grid[i][j] != '1':
8                return 
9            
10            else:
11                grid[i][j] = '0'
12                dfs(i -1, j)
13                dfs(i+1, j)
14                dfs(i, j-1)
15                dfs(i, j+1)
16        
17        for i in range(n):
18            for j in range(m):
19                if grid[i][j] == '1':
20                    cnt += 1
21                    dfs(i, j)
22        
23        return cnt
24                