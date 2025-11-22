# Last updated: 11/21/2025, 8:46:45 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        {100, 4, 200, 1, 3, 2, 101, 102}
        i = 0, 1, 2, 4
        100 - 
        200 - 
        1 - 2 - 3 - 4
        """

        numset = set(nums)
        res = 0

        for num in numset: 
            length = 0
            if num - 1 not in numset:
                while num + length in numset:
                    length += 1
            else:
                continue
            res = max(res, length)
        
        return res