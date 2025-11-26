# Last updated: 11/26/2025, 11:51:51 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        
9        a = list1
10        b = list2
11        temp = ListNode()
12        res = temp
13
14        while a and b:
15            if a.val <= b.val:
16                res.next = a
17                a = a.next
18            else:
19                res.next = b
20                b = b.next
21            res = res.next
22        
23        res.next = a if a else b
24        
25        return temp.next
26