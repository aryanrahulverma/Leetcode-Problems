# Last updated: 11/27/2025, 12:48:06 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        p1, p2 = dummy, dummy

        if p1.next == None:
            return None
        
        for _ in range(n):
            p2 = p2.next
        
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next
        
        p1.next = p1.next.next

        return dummy.next