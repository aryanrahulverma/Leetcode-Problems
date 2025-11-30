# Last updated: 11/30/2025, 5:01:43 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3
4        temp = []
5
6        for c in s:
7            if c.isalnum():
8                temp.append(c)
9
10        p1, p2 = 0, len(temp) - 1
11
12        while p1 <= p2:
13            if temp[p1].lower() != temp[p2].lower():
14                return False
15            
16            p1 += 1
17            p2 -= 1
18        
19        return True