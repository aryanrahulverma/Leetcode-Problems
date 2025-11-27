# Last updated: 11/26/2025, 9:58:44 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        fast = head
10        slow = head
11        
12        while fast and fast.next:
13            fast = fast.next.next
14            slow = slow.next
15            
16            if fast == slow:
17                return True
18    
19        return False