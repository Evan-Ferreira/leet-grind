class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        tmp = []
        for i in range(len(names)):
            tmp.append([heights[i], names[i]])
        
        tmp.sort(key=lambda x : -x[0])
        return [n for h, n in tmp]