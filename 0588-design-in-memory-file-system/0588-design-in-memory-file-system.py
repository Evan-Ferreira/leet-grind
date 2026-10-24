class Node:
    def __init__(self, name = "", isFile = False):
        self.isFile = isFile
        self.name = name
        self.children = defaultdict(Node)
        self.content = ""

class FileSystem:
    def __init__(self):
        self.root = Node("/")
    
    def _navigate(self, path):
        directories = path.split('/')[1:]
        curr = self.root

        if len(directories) == 1 and directories[0] == "":
            return curr

        for d in directories:
            curr = curr.children[d]
            curr.name = d
        return curr

    def ls(self, path: str) -> list[str]:
        curr = self._navigate(path)
        print(path, curr.name)
        if curr.isFile:
            return [curr.name]
        return sorted(curr.children.keys())

    def mkdir(self, path: str) -> None:
        self._navigate(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self._navigate(filePath)
        curr.isFile = True
        curr.content += content

    def readContentFromFile(self, filePath: str) -> str:
        curr = self._navigate(filePath)
        return curr.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)