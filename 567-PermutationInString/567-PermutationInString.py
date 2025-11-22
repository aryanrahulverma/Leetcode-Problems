# Last updated: 11/21/2025, 8:46:38 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_mp = self.createDictionary(s1)
        s1_len = len(s1)

        l = 0
        r = s1_len - 1

        while r < len(s2):
            window = self.createDictionary(s2[l:r+1])
            if window == s1_mp:
                return True
            r += 1
            l += 1
        
        return False

    
    def createDictionary(self, s):
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        
        return freq