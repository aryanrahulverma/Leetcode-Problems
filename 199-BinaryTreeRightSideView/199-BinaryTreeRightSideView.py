# Last updated: 12/2/2025, 7:02:21 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
9        q = []
10        res = []
11
12        if not root:
13            return []
14
15        q.append(root)
16
17        while q:
18            n = len(q)
19            for _ in range(n):
20                node = q.pop(0)
21
22                if _ == (n - 1):
23                    res.append(node.val)
24
25                if node.left: q.append(node.left)
26                if node.right: q.append(node.right)
27        
28        return res
29            