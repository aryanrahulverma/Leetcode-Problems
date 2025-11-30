# Last updated: 11/30/2025, 11:05:58 AM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        
4        def toDict(s):
5            hashmp = defaultdict(int)
6
7            for c in s:
8                hashmp[c] += 1
9            
10            return hashmp
11        
12        return toDict(s) == toDict(t)
13