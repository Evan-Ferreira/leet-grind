class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)

        for b in bills:
            diff = b - 5
            change[b] += 1
            for c in [10, 5]:
                needs = diff // c
                if (change[c] - needs) >= 0:
                    change[c] -= needs
                    diff -= needs * c
            if diff > 0:
                return False
        return True