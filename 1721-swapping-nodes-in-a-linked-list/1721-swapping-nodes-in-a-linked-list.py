# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prevHead = ListNode()
        prevHead.next = head
        prevFirstNode = prevHead
        curr = prevFirstNode
        count = 0
        while curr:
            if count == (k - 1):
                prevFirstNode = curr
            curr = curr.next
            count += 1  

        if count == 2:
            return head

        second = count - k
        curr = prevHead
        count = 0

        while curr:
            if count == (second - 1):
                prevSecondNode = curr
                secondNode = prevSecondNode.next
                firstNode = prevFirstNode.next
                prevFirstNode.next = secondNode
                prevSecondNode.next = firstNode
                secondNodeNext = secondNode.next
                secondNode.next = firstNode.next
                firstNode.next = secondNodeNext
                
                return prevHead.next
            curr = curr.next
            count += 1
        
