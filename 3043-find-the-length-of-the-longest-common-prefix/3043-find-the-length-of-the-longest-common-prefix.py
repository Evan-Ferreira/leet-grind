class Node:
    def __init__(self):
        self.children = defaultdict(Node)

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
    
    def getCount(self, word):
        curr = self.root
        count = 0
        for char in word:
            if char not in curr.children:
                break
            curr = curr.children[char]
            count += 1  
        return count

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = [str(i) for i in arr1]
        arr2 = [str(i) for i in arr2]

        res = 0
        trie = Trie()

        for s in arr2:
            trie.insert(s)
        
        for s in arr1:
            res = max(res, trie.getCount(s))
        
        return res
        

        