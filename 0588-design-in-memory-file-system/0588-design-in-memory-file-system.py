class Node:
    def __init__(self):
        self.name = ""
        self.isFile = False
        self.content = ""
        self.children = defaultdict(Node)

class FileSystem:

    def __init__(self):
        self.root = Node()
    
    def _insert(self, path):
        path = [] if len(path) == 1 else path.split("/")[1:]
        curr = self.root
        for p in path:
            curr = curr.children[p]
            curr.name = p
        return curr

    def ls(self, path: str) -> list[str]:
        curr = self._insert(path)
        return [curr.name] if curr.isFile else sorted(curr.children.keys())

    def mkdir(self, path: str) -> None:
        self._insert(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self._insert(filePath)
        curr.isFile = True
        curr.content += content

    def readContentFromFile(self, filePath: str) -> str:
        curr = self._insert(filePath)
        return curr.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)