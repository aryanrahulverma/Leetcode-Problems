# Last updated: 11/27/2025, 10:49:31 AM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)

        l, r = 1, res

        while l <= r:
            
            m = (l + r) // 2
            calc = 0

            for i in piles:
                calc += (i + m - 1) // m

            if calc <= h:
                r = m - 1
                res = m

            else:
                l = m + 1
    
        return res
            
        
