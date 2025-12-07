# Last updated: 12/6/2025, 9:17:21 PM
1class Solution:
2    def countGoodSubstrings(self, s: str) -> int:
3        cnt = 0
4
5        if len(s) < 3:
6            return 0
7
8        for i in range(0, len(s) - 2):
9            a = s[i]
10            b = s[i + 1]
11            c = s[i + 2]
12
13            if a!=b and a!=c and b!=c:
14                cnt += 1
15            
16        return cnt
17
18