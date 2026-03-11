class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        start = sorted([pos - ran for pos, ran in lights])
        end = sorted([pos + ran for pos, ran in lights])

        i = start[0]
        res = count = 0
        s = e = 0

        while s < len(lights) and e < len(lights):
            if start[s] <= end[e]:
                count += 1
                if count > res:
                    i = start[s]
                    res = count
                s += 1
            else:
                e += 1
                count -= 1
        return i

        