class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def getTotalDays(arr):
            month, day = arr.split("-")
            month, day = int(month), int(day)
            total_month_days = 0
            for i in range(month - 1):
                total_month_days += MONTH_DAYS[i]
            return total_month_days + day

        arriveAliceDays = getTotalDays(arriveAlice)
        leaveAliceDays = getTotalDays(leaveAlice)
        arriveBobDays = getTotalDays(arriveBob)
        leaveBobDays = getTotalDays(leaveBob)

        print(arriveAliceDays, leaveAliceDays)
        print(arriveBobDays, leaveBobDays)

        if leaveAliceDays < arriveBobDays or leaveBobDays < arriveAliceDays:
            return 0
        elif arriveAliceDays <= arriveBobDays and leaveAliceDays >= leaveBobDays:
            return leaveBobDays - arriveBobDays + 1
        elif arriveBobDays <= arriveAliceDays and leaveBobDays >= leaveAliceDays:
            return leaveAliceDays - arriveAliceDays + 1
        elif arriveAliceDays < arriveBobDays and leaveAliceDays <= leaveBobDays:
            return leaveAliceDays - arriveBobDays + 1
        elif arriveBobDays < arriveAliceDays and leaveBobDays <= leaveAliceDays:
            return leaveBobDays - arriveAliceDays + 1
        else:
            return leaveBobDays - arriveAliceDays + 1