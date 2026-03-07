class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        res = []
        possibilities = [['6', '9'], ['9', '6'], ['1', '1'], ['0', '0'], ['8', '8']]
        def dfs(curr):
            if len(curr) == n:
                res.append(curr)
                return
            
            for leftChar, rightChar in possibilities:
                if n % 2 == 1 and curr == "":
                    if leftChar not in ['6', '9']:
                        dfs(leftChar)
                else:
                    if not (len(curr) + 2 == n and leftChar == '0'):
                        dfs(leftChar + curr + rightChar)

        dfs("")
        return res
            




        
        