class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        
        if n == 2:
            return 1
        # [1, 1, 2, 4]   
        q = deque([0, 1, 1])
        for i in range(2, n):
            res = sum(q)
            q.append(res)
            q.popleft()
        return q[-1]     