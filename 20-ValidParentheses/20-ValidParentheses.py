# Last updated: 11/21/2025, 8:46:48 PM
class Solution:
    def isValid(self, s: str) -> bool:
        mp = {')':'(',
              '}':'{',
              ']':'['    
            }
            
        if len(s) == 1:
            return False

        stack = []

        for i in s:
            if i in {'(', '{', '['}:
                stack.append(i)

            elif stack and stack[-1] == mp[i]:
                stack.pop()
            
            else: 
                return False

        if not stack:
            return True
        else:
            return False