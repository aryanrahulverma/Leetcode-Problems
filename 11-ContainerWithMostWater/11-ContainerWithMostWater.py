# Last updated: 11/30/2025, 6:24:39 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        
4        l, r = 0, len(height) - 1
5        a = 0
6        res = 0
7
8        while l < r:
9            a = min(height[r], height[l]) * (r - l)
10            if height[l] > height[r]:
11                r -= 1
12            else:
13                l += 1
14            
15            res = max(res, a)
16        
17        return res