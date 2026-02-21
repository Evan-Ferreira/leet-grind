class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordMap = {}

        for i in range(len(order)):
            ordMap[order[i]] = i

        for i in range(1, len(words)):
            length = min(len(words[i]), len(words[i - 1]))
            for p in range(length):
                if ordMap[words[i][p]] > ordMap[words[i - 1][p]]:
                    break
                elif ordMap[words[i][p]] == ordMap[words[i - 1][p]]:
                    continue
                else:
                    return False
            length1, length2 = len(words[i - 1]), len(words[i])
            if words[i][:length] == words[i - 1][:length] and length1 > length2:
                return False
        return True