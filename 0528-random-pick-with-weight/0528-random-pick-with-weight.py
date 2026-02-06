class Solution:
    def __init__(self, w: List[int]):
        self.prefix = [0]
        for wgt in w:
            self.prefix.append(self.prefix[-1] + wgt)

    def pickIndex(self) -> int:
        target = random.uniform(0, self.prefix[-1])
        l, r = 0, len(self.prefix)

        while l < r:
            mid = (l + r) // 2
            if self.prefix[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l - 1
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()