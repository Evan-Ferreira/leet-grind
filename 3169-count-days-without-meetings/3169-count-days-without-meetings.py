class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        res = 0
        meetings.append([0, 0])
        meetings.append([days + 1, days + 1])
        meetings.sort()

        endMax = meetings[0][1]
        for start, end in meetings:
            if start - endMax > 1:
                res += start - endMax - 1
            endMax = max(endMax, end) 

        return res


            