# Last updated: 11/30/2025, 11:14:12 AM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3
4        sub = defaultdict(int)
5
6        for i in range(len(nums)):
7            diff = (target - nums[i])
8            if diff in sub:
9                return [i, sub[diff]]
10            else:
11                sub[nums[i]] = i