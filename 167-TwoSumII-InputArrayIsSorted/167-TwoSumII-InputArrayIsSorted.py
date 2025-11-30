# Last updated: 11/30/2025, 5:43:49 PM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        l, r = 0, len(numbers) - 1
4
5        while l <= r:
6            addn = numbers[r] + numbers[l] 
7
8            if addn < target:
9                l += 1
10            elif addn > target:
11                r -= 1
12            else:
13                return [l + 1, r + 1]
14
15
16            
17