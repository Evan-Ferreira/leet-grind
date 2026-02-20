class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        curr = 0
        d = {0: [0, 1], 1: [1, 0]}
        maxK = 2 ** (n - 1)
        minK = 0
        mid = maxK // 2
        for _ in range(n - 1):
            if k <= mid:
                curr = d[curr][0]
                maxK = mid
                mid = (minK + mid) // 2
            else:
                curr = d[curr][1]
                minK = mid
                mid = (mid + maxK) // 2
        return curr
            