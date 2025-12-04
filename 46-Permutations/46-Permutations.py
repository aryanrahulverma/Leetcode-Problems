# Last updated: 12/3/2025, 6:04:23 PM
1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        res, sub = [], []
4        n = len(nums)
5
6        def backtrack():
7            if len(sub) == n:
8                res.append(sub.copy())
9                return
10
11            for i in nums:
12                if i not in sub:
13                    sub.append(i)
14                    backtrack()
15                    sub.pop()
16        
17        backtrack()
18
19        return res