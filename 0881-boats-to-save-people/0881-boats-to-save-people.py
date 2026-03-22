class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l, r = 0, len(people) - 1
        res = curr = hc = 0

        while l <= r:
            if curr + people[r] <= limit and hc != 2:
                curr += people[r]
                r -= 1
                hc += 1
            
            elif curr + people[l] <= limit and hc != 2:
                curr += people[l]
                l += 1
                hc += 1
            
            else:
                res += 1
                curr = 0
                hc = 0
                
        if curr > 0:
            res += 1
        
        return res