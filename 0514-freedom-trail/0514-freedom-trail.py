class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        characters = defaultdict(list)
        N = len(ring)
        for i, char in enumerate(ring):
            characters[char].append(i)
        
        dp = {}

        def dfs(char_index, circle_index):
            if char_index == len(key):
                return 0

            if (char_index, circle_index) in dp:
                return dp[(char_index, circle_index)]

            dp[(char_index, circle_index)] = float('inf')
            for i in characters[key[char_index]]:
                distance = (i - circle_index) % N
                dp[(char_index, circle_index)] = min(dp[(char_index, circle_index)], dfs(char_index + 1, i) + min(distance, N - distance) + 1)

            
            return dp[(char_index, circle_index)]
        
        return dfs(0, 0)


        