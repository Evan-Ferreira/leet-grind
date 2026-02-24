class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        def removeNode(node):
            prev, nxt = node.prev, node.next
            prev.next = nxt
            nxt.prev = prev

        root = Node(1)
        node = root
        for num in range(2, n + 1):
            newNode = Node(num)
            node.next = newNode
            newNode.prev = node
            node = newNode
        node.next = root
        root.prev = node

        curr = root
        while curr.next != curr:
            for _ in range(k - 1):
                curr = curr.next
            nxt = curr.next
            removeNode(curr)
            curr = nxt

        return curr.val

            
