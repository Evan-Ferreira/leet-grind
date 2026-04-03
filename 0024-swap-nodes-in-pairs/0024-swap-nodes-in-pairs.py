# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        if not head or not head.next:
            return head

        prev = dummy
        curr = head
        while curr and curr.next:
            nxt = curr.next
            tmp = nxt.next
            prev.next = nxt
            nxt.next = curr
            curr.next = tmp
            prev = curr
            curr = curr.next

        return dummy.next

            




