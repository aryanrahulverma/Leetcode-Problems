# Last updated: 12/6/2025, 9:57:18 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
9        indexmp = {}
10        ind = 0
11
12        if not head:
13            return None
14
15        slow = head
16        indexmp[slow] = 0
17
18        while slow and slow.next:
19            curr = slow
20            slow = slow.next
21            if slow not in indexmp:
22                indexmp[slow] = ind
23                ind += 1
24                
25            else:
26                return slow
27            
28        return None
29            
30
31            
32
33        
34
35
36