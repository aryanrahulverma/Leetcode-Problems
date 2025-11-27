# Last updated: 11/27/2025, 10:49:07 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reorderList(self, head: Optional[ListNode]) -> None:
8        """
9        Do not return anything, modify head in-place instead.
10        """
11        
12        slow, fast = head, head.next
13
14        #find middle
15        while fast and fast.next:
16            slow = slow.next
17            fast = fast.next.next
18        
19        second = slow.next
20        prev = slow.next = None
21
22        # reverse second half
23        while second:
24            nxt = second.next
25            second.next = prev
26            prev = second
27            second = nxt
28        
29        first, sec = head, prev
30
31        #merge first and second half
32        while first and sec:
33            nxt1 = first.next
34            nxt2 = sec.next
35            first.next = sec
36            sec.next = nxt1
37            first, sec = nxt1, nxt2
38