class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if not stack or a > 0 or (stack and stack[-1] < 0):
                stack.append(a)
                continue
            elif stack and abs(stack[-1]) == abs(a):
                stack.pop()
                continue
            while stack and stack[-1] > 0 and abs(a) > stack[-1]:
                stack.pop()
            if not stack or (stack and stack[-1] < 0):
                stack.append(a)
            elif stack and stack[-1] == abs(a) and stack[-1] > 0 and a < 0:
                stack.pop()
        return stack