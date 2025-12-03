# Last updated: 12/2/2025, 10:31:52 PM
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        sol = []
4        sub = []
5        n = len(nums)
6
7        def dfs(i):
8            if i == n:
9                sol.append(sub.copy())
10                return
11            
12            nxt = nums[i]
13
14            dfs(i + 1)
15
16            sub.append(nxt)
17            dfs(i + 1)
18
19            sub.pop()
20        
21        dfs(0)
22        
23        return sol
24