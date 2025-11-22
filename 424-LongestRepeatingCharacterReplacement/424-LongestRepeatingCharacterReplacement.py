# Last updated: 11/21/2025, 8:46:39 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0
        l = 0
        mp = defaultdict(int)

        for r in range(len(s)):
            mp[s[r]] += 1

            if (r - l + 1) - max(mp.values()) > k:
                mp[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
