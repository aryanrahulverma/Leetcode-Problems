# Last updated: 11/27/2025, 4:23:43 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        def dfs(root):
10            if not root:
11                return [0, True]
12            
13            l, r = dfs(root.left), dfs(root.right)
14
15            balance = (l[1] and r[1] and abs(l[0] - r[0]) <= 1)
16            return [1 + max(l[0], r[0]), balance]
17        
18        return dfs(root)[1]