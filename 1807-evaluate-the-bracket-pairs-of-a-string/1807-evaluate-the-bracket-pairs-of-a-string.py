class TrieNode:
    def __init__(self, char = None):
        self.children = defaultdict(TrieNode)
        self.value = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, key, value):
        node = self.root
        for char in key:
            node = node.children[char]
        node.value = value

class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        trie = Trie()
        for key, value in knowledge:
            trie.insert(key, value)
        
        N = len(s)
        res = []
        l = 0
        for r in range(N):
            if s[l] == "(" and s[r] == ")":
                l += 1
                node = trie.root
                while l != r:
                    if s[l] in node.children:
                        node = node.children[s[l]]
                        l += 1
                    else:
                        break
                if l == r and node.value:
                    res += node.value
                else:
                    res.append("?")
                l = r
            elif s[l] == "(":
                if r == len(s) - 1:
                    res += s[l:].split()
                    break
            else:
                if s[r] != "(":
                    res.append(s[r])
                l += 1
        return "".join(res)
            
                
            
            
        
        
            
            
                    
        
        