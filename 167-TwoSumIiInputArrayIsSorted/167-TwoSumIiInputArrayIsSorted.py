# Last updated: 11/30/2025, 5:44:15 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l <= r:
            addn = numbers[r] + numbers[l] 

            if addn < target:
                l += 1
            elif addn > target:
                r -= 1
            else:
                return [l + 1, r + 1]


            
