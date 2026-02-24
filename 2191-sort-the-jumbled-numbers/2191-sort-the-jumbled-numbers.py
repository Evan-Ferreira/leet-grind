class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        h = []
        heapq.heapify(h)
        res = []

        for i, n in enumerate(nums):
            number = 0
            power = 0
            if n == 0:
                bypass = True
            while n or bypass:
                bypass = False
                digit = n % 10
                number += (mapping[digit] * (10 ** power))
                power += 1
                n //= 10
            heapq.heappush(h, (number, i))

        while h:
            _, i = heapq.heappop(h)
            res.append(nums[i])
        
        return res
            



