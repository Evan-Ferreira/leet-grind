# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        def removeNode(prevNode):
            nxt = prevNode.next.next
            node = prevNode.next
            node.next = None
            prevNode.next = nxt
        
        def insertNode(prevNode, newNode):
            nxt = prevNode.next
            prevNode.next = newNode
            newNode.next = nxt
        
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        q = deque()
        while curr and curr.next:
            if curr.next.val < x:
                q.append(curr.next)
                removeNode(curr)
            else:
                curr = curr.next
        
        curr = dummy
        while q:
            newNode = q.popleft()
            if not curr.next or newNode.val < curr.next.val:
                insertNode(curr, newNode)
            curr = curr.next
        
        return dummy.next
        



            
            
            
