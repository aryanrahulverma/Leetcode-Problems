# Last updated: 11/27/2025, 11:26:26 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        
9        dummy = ListNode(0, head)
10        p1, p2 = dummy, dummy
11
12        if p1.next == None:
13            return None
14        
15        for _ in range(n):
16            p2 = p2.next
17        
18        while p2 and p2.next:
19            p1 = p1.next
20            p2 = p2.next
21        
22        p1.next = p1.next.next
23
24        return dummy.next