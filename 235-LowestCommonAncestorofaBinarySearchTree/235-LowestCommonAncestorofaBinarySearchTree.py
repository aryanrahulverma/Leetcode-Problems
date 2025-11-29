# Last updated: 11/29/2025, 10:57:47 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        
11        curr = root
12
13        while curr:
14            if p.val > curr.val and q.val > curr.val:
15                curr = curr.right
16            elif p.val < curr.val and q.val < curr.val:
17                curr = curr.left
18            else:
19                return curr
20