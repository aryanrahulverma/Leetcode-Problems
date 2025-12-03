# Last updated: 12/2/2025, 8:59:38 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        maxVal = root.val
        self.cnt = 0

        def dfs(root, maxVal):
            if not root:
                return None

            if root.val >= maxVal:
                maxVal = root.val
                self.cnt += 1
            
            dfs(root.left, maxVal)
            dfs(root.right, maxVal)

        dfs(root, maxVal)

        return self.cnt
            