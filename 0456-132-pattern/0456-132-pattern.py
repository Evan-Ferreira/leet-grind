class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack = []
        last = float('-inf')
        for n in nums[::-1]:
            if last > n:
                return True

            while stack and stack[-1] < n:
                last = stack[-1]
                stack.pop()
            stack.append(n)
        return False
        
