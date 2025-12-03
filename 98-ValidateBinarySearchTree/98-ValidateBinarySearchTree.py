# Last updated: 12/2/2025, 8:59:30 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: Optional[TreeNode]) -> bool:
9
10        if not root:
11            return True
12
13        q = []
14
15        q.append((root, float("-inf"), float("inf")))
16
17        while q:
18            node, l, r = q.pop(0)
19
20            if not (l < node.val < r):
21                return False
22
23            if node.left: q.append((node.left, l, node.val))               
24            if node.right: q.append((node.right, node.val, r)) 
25
26        return True