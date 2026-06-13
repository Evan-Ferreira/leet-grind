# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mx = head.val
        tmp = head
        while tmp:
            mx = max(tmp.val, mx)
            tmp = tmp.next

        primes = []
        not_primes = set()
        for i in range(2, mx + 1):
            if i not in not_primes:
                primes.append(i)
                n = i
                for j in range(i, mx):
                    if j * i > mx:
                        break
                    not_primes.add(j * i)

        def getGCD(n1, n2):
            start = 1
            for p in primes[::-1]:
                if n1 % p == 0 and n2 % p == 0:
                    start = p
                    break
            if start == 1:
                return 1
            new = start
            for i in range(2, min(n1, n2)):
                if start * i > min(n1, n2):
                    break
                if n1 % (start * i) == 0 and n2 % (start * i) == 0:
                    new = start * i
            return new

        prev = head
        curr = head.next
        while curr:
            new = ListNode()
            new.val = getGCD(prev.val, curr.val)
            prev.next = new
            new.next = curr
            prev = curr
            curr = curr.next
        
        return head