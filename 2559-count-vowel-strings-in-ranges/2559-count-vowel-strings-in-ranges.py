class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0] * (len(words) + 1)
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        res = [0] * len(queries)
        
        for i in range(len(words)):
            prefix[i + 1] = prefix[i] + (1 if words[i][0] in vowels and words[i][-1] in vowels else 0)
        print(prefix)
        for index in range(len(queries)):
            l, r = queries[index][0], queries[index][1]
            res[index] = prefix[r + 1] - prefix[l]
        
        return res
