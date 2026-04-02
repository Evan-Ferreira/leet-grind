class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        sums = defaultdict(list)
        
        res = []
        for i in range(N):
            for j in range(i + 1, N):
                sums[nums[i] + nums[j]].append([i, j])

        keys = sorted(sums.keys(), reverse=True)
        for k in keys:
            l, r = 0, N - 1
            while (l + 1) < (r - 1):
                first_sum = nums[l] + nums[r]
                need = target - first_sum
                if need < k:
                    r -= 1
                    while (l + 1) < (r - 1) and nums[r] == nums[r + 1]:
                        r -= 1
                elif need > k:
                    l += 1
                    while (l + 1) < (r - 1) and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    prevL = len(res)
                    for i, j in sums[need]:
                        if (len(res) > prevL and ((res[-1][1] == nums[i] 
                            and res[-1][2] == nums[j]) or (res[-1][1] == nums[j] 
                            and res[-1][2] == nums[i]))):
                            continue

                        if l < i < r and l < j < r:
                            res.append([nums[l], nums[i], nums[j], nums[r]])
                    l += 1
                    while (l + 1) < (r - 1) and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while (l + 1) < (r - 1) and nums[r] == nums[r + 1]:
                        r -= 1

        return res