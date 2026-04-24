class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        curr = []
        def backtrack(i):
            nonlocal curr
            nonlocal res

            if len(curr) == k:
                res.append(curr.copy())
                return
            
            if i == (n + 1):
                return
            
            curr.append(i)
            backtrack(i + 1)
            curr.pop()
            backtrack(i + 1)
        
        backtrack(1)
        return res