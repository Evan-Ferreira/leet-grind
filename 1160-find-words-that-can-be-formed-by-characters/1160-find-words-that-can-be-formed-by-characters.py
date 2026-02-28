class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charD = defaultdict(int)
        res = 0
        for c in chars:
            charD[c] += 1
        
        for w in words:
            curr = defaultdict(int)
            for i in range(len(w)):
                curr[w[i]] += 1
            
            addToRes = True
            for key, value in curr.items():
                if value > charD[key]:
                    addToRes = False
                    break
            if addToRes:
                res += len(w)
        return res
            
        

        
