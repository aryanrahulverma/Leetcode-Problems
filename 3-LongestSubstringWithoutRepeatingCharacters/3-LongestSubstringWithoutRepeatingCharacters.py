# Last updated: 12/6/2025, 8:20:10 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        
4        l, r = 0, 0
5        length = 0
6        seen = set()
7
8        if s == '':
9            return 0
10        
11        while r < len(s):
12            if s[r] in seen:
13                while s[l] != s[r]:
14                    seen.remove(s[l])
15                    l += 1
16                l += 1
17                r += 1
18            
19            else:
20                seen.add(s[r])
21                length = max(length, r - l + 1)
22                r += 1
23    
24        return length
25            
26
27            
28            