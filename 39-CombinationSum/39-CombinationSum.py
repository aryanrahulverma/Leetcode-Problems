# Last updated: 12/3/2025, 4:02:55 PM
1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        sol = []
4        sub = []
5        n = len(candidates)
6
7        def backtrack(i, addn):
8            if addn == target:
9                sol.append(sub.copy())
10                return
11            
12            if addn > target or i == n:
13                return
14            
15            backtrack(i + 1, addn)
16
17            sub.append(candidates[i])
18            backtrack(i, addn + candidates[i])
19            sub.pop()
20
21        backtrack(0, 0)
22
23        return sol