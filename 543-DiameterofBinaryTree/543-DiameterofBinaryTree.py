# Last updated: 11/27/2025, 1:17:58 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9        self.res = 0
10
11        def dfs(root):
12            if not root:
13                return 0
14            
15            left = dfs(root.left)
16            right = dfs(root.right)
17
18            self.res = max(self.res, (left + right))
19
20            return 1 + max(left, right)
21        
22        dfs(root)
23        return self.res