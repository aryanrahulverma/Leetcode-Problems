# Last updated: 11/21/2025, 8:46:40 PM
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        right, left = len(s)-1, 0

        while right > left:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        

        
