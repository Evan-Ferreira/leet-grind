class Node:
    def __init__(self):
        self.name = ""
        self.isFile = False
        self.content = ""
        self.children = defaultdict(Node)

class FileSystem:

    def __init__(self):
        self.root = Node()

    def ls(self, path: str) -> list[str]:
        path = [] if len(path) == 1 else path.split("/")[1:]
        curr = self.root
        for p in path:
            curr = curr.children[p]
            curr.name = p
        return [curr.name] if curr.isFile else sorted(curr.children.keys())

    def mkdir(self, path: str) -> None:
        path = [] if len(path) == 1 else path.split("/")[1:]
        curr = self.root
        for p in path:
            curr = curr.children[p]
            curr.name = p
            

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = [] if len(filePath) == 1 else filePath.split("/")[1:]
        curr = self.root
        for p in path:
            curr = curr.children[p]
            curr.name = p
        curr.isFile = True
        curr.content += content

    def readContentFromFile(self, filePath: str) -> str:
        path = [] if len(filePath) == 1 else filePath.split("/")[1:]
        curr = self.root
        for p in path:
            curr = curr.children[p]
            curr.name = p
        return curr.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)