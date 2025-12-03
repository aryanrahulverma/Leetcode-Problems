# Last updated: 12/2/2025, 7:22:49 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def goodNodes(self, root: TreeNode) -> int:
9        if not root:
10            return 0
11
12        maxVal = root.val
13        self.cnt = 0
14
15        def dfs(root, maxVal):
16            if not root:
17                return None
18
19            if root.val >= maxVal:
20                maxVal = root.val
21                self.cnt += 1
22            
23            dfs(root.left, maxVal)
24            dfs(root.right, maxVal)
25
26        dfs(root, maxVal)
27
28        return self.cnt
29            