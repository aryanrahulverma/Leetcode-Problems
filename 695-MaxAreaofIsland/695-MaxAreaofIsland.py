# Last updated: 12/5/2025, 6:59:39 PM
1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        area = 0
4       
5        m, n = len(grid), len(grid[0])
6
7        def dfs(i, j):
8            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 1:
9                return
10            
11            else:
12                grid[i][j] = 0
13                self.temp += 1
14                dfs(i+1,j)
15                dfs(i-1,j)
16                dfs(i,j+1)
17                dfs(i,j-1)
18        
19        for i in range(m):
20            for j in range(n):
21                if grid[i][j] == 1:
22                    self.temp = 0
23                    dfs(i, j)
24                    area = max(area, self.temp)
25                    
26
27        return area
28        
29