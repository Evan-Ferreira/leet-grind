class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        N = len(A)
        img1 = [(i, j) for i in range(N) for j in range(N) if A[i][j] == 1]
        img2 = [(i, j) for i in range(N) for j in range(N) if B[i][j] == 1]

        count = [[0] * (2 * N) for _ in range(2 * N)]
        res = 0
        for ax, ay in img1:
            for bx, by in img2:
                dx = bx - ax + N
                dy = by - ay + N
                count[dx][dy] += 1
                res = max(res, count[dx][dy])
        return res