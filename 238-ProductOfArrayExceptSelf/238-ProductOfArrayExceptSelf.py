# Last updated: 11/21/2025, 8:46:43 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = [1] * len(nums)
        prod = 1

        for i in range(len(nums)):
            temp[i] *= prod
            prod *= nums[i]

        prod = 1

        for i in range(len(nums) -1, -1, -1):
            temp[i] *= prod
            prod *= nums[i]
        
        return temp