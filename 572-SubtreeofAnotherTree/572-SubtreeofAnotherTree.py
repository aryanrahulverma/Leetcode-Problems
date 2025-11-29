# Last updated: 11/29/2025, 10:33:05 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
9    
10        if not root:
11            return False
12        if not subRoot:
13            return True
14        
15        if self.isSameTree(root, subRoot):
16            return True
17        
18        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
19
20    def isSameTree(self, a, b):
21        if not a and not b:
22            return True
23        
24        elif a and b:
25            return (a.val == b.val) and self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)
26
27        else:
28            return False