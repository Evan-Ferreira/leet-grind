"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        new = Node(insertVal)
        oldHead = head
        if not head:
            new.next = new
            return new


        curr = head.next
        here = head
        while curr.val <= curr.next.val and head != curr:
            curr = curr.next

        if curr.val > curr.next.val:
            head = curr.next
        
        curr = head
        new = Node(insertVal)
        while curr.next != head:
            if curr.val <= insertVal <= curr.next.val:
                nxt = curr.next
                curr.next = new
                new.next = nxt
                return oldHead
            curr = curr.next

        curr.next = new
        new.next = head
        return oldHead
                