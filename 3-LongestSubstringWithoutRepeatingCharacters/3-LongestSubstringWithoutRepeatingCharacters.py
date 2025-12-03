# Last updated: 12/2/2025, 6:39:46 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        # res = []
10
11        # def dfs(root, d):
12        #     if not root: 
13        #         return None
14            
15        #     if len(res) == d:
16        #         res.append([])
17
18        #     res[d].append(root.val)
19        #     dfs(root.left, d + 1)
20        #     dfs(root.right, d + 1)
21        
22        # dfs(root, 0)
23
24        # return res
25
26        q = []
27        res = []
28
29        if not root:
30            return []
31
32        q.append(root)
33
34        while q:
35            temp = []
36            for _ in range(len(q)):
37                node = q.pop(0)
38
39                if node.left: q.append(node.left)
40                if node.right: q.append(node.right)
41
42                temp.append(node.val)
43            
44            res.append(temp)
45        
46        return res