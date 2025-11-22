# Last updated: 11/21/2025, 8:46:40 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        res = s

        for i in range(k, len(nums)):
            s = s - nums[i-k] + nums[i]
            res = max(res, s)
            
        return res/k
    