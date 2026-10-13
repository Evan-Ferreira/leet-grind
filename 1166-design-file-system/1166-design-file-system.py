class TrieNode:
    def __init__(self):
        self.val = None
        self.children = defaultdict(TrieNode)

class FileSystem:
    def __init__(self):
        self.root = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        directories = path.split("/")[1:]
        curr = self.root
        for i, d in enumerate(directories):
            if d not in curr.children and i != (len(directories) - 1):
                return False
            curr = curr.children[d]
        if curr.val != None:
            return False
        curr.val = value
        return True
        
    def get(self, path: str) -> int:
        directories = path.split("/")[1:]
        curr = self.root
        for d in directories:
            if d not in curr.children:
                return -1
            curr = curr.children[d]
        return -1 if curr.val == None else curr.val


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)