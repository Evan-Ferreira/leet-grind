class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        D, R = deque(), deque()

        for i, s in enumerate(senate):
            if s == 'D':
                D.append(i)
            else:
                R.append(i)
        
        while D and R:
            dTurn, rTurn = D.popleft(), R.popleft()

            if rTurn < dTurn:
                R.append(dTurn + len(senate))
            else:
                D.append(rTurn + len(senate))
        
        return "Radiant" if R else "Dire"