# Last updated: 11/25/2025, 9:37:25 AM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1, l2 = 0, 0
        r2, r1 = len(matrix[0])-1, 0

        while r1 < len(matrix):
            if target > matrix[r1][r2]:
                r1+=1
                l1+=1
            else:
                break

        if r1 == len(matrix):
            return False
        
        while l2 <= r2:
            m = (l2 + r2) // 2
            print(m)
            if matrix[l1][m] == target:
                return True
            elif matrix[l1][m] > target:
                r2 = m - 1 
            else:
                l2 = m + 1


        return False