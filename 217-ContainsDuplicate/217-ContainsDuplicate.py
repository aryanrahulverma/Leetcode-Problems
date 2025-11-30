# Last updated: 11/30/2025, 11:03:44 AM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        duplicates = set()
4
5        for i in nums: 
6            if i in duplicates:
7                return True
8            else:
9                duplicates.add(i)
10            
11        return False