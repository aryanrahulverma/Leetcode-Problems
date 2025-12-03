# Last updated: 12/2/2025, 9:32:58 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        self.arr = []
10
11        def dfs(root):
12            if not root:
13                return None
14
15            dfs(root.left)
16            self.arr.append(root.val)
17            dfs(root.right)
18
19        dfs(root)
20
21        return self.arr[k-1]