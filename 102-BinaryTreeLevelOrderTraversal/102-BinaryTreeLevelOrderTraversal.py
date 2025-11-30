# Last updated: 11/29/2025, 8:35:45 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        res = []
10
11        def dfs(root, d):
12            if not root: 
13                return None
14            
15            if len(res) == d:
16                res.append([])
17
18            res[d].append(root.val)
19            dfs(root.left, d + 1)
20            dfs(root.right, d + 1)
21        
22        dfs(root, 0)
23
24        return res