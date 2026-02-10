class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = 0
        for l in logs:
            if l == "../":
                if stack:
                    stack -= 1
                else:
                    continue
            elif l == "./":
                continue
            else:
                stack += 1
        return stack