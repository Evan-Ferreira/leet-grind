class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        N = len(arr)
        if N == 1:
            return -1
        
        matches = []
        prefixSum = [0] * N
        for i in range(N):
            prefixSum[i] = arr[0] if i == 0 else arr[i] + prefixSum[i - 1]
        
        l = -1
        for r in range(N):
            while l <= r:
                subtract = 0 if l == -1 else prefixSum[l]
                s = prefixSum[r] - subtract
                if s == target:
                    matches.append([l + 1, r])
                    break
                elif s > target:
                    l += 1
                else:
                    break

        N = len(matches)
        postMinLength = [0] * N
        res = float('inf')
        for i in range(N):
            if i == 0:
                postMinLength[N - 1 - i] = matches[N - 1 - i][1] - matches[N - 1 - i][0] + 1
            else:
                postMinLength[N - 1 - i] = min(matches[N - 1 - i][1] - matches[N - 1 - i][0] + 1, postMinLength[N - i])
        print(matches)
        print(postMinLength)
        matchI= 1
        for i in range(N - 1):
            beg1, end1 = matches[i]
            beg2, end2 = matches[matchI]
            while beg2 <= end1 and matchI < (N - 1):
                matchI += 1
                beg2, end2 = matches[matchI]
            if beg2 <= end1:
                break
            res = min(res, (end1 - beg1 + 1) + postMinLength[matchI])
        return -1 if res == float('inf') else res
        
