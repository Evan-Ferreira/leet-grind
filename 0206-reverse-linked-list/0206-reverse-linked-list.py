# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        node = head
        prev = None
        if not head:
            return
        while node.next != None:
            n = node.next
            node.next = prev
            prev = node
            node = n
        node.next = prev
        return node