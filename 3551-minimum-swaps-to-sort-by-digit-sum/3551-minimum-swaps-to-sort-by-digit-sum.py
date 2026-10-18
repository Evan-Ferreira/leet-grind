class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        digit_sum = lambda x: sum(map(int, str(x)))
        rank ={ x: i for i, x in enumerate(sorted(nums, key=lambda x: (digit_sum(x), x)))}
        order = [rank[n] for n in nums]

        swaps = 0
        for i in range(len(nums)):
            while order[i] != i:
                j = order[i]
                order[i], order[j] = order[j], order[i]
                swaps += 1
        return swaps