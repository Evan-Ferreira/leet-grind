class TokenNode:
    def __init__(self, tokenId, currentTime):
        self.prev = None
        self.next = None
        self.tokenId = tokenId
        self.currentTime = currentTime

class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.left = TokenNode("", 0)
        self.right = TokenNode("", 0)
        self.tokenToNode = {}
        self.left.next = self.right
        self.right.prev = self.left
        self.length = 0

    def generate(self, tokenId: str, currentTime: int) -> None:
        new = TokenNode(tokenId, currentTime)
        prev = self.right.prev
        prev.next = new
        self.right.prev = new
        new.prev = prev
        new.next = self.right
        self.length += 1
        self.tokenToNode[tokenId] = new

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokenToNode:
            node = self.tokenToNode[tokenId]
            if (currentTime - node.currentTime) >= self.timeToLive:
                prev = node.prev 
                prev.next = node.next
                node.next.prev = prev
                del self.tokenToNode[tokenId]
                self.length -= 1
            else:
                old = self.tokenToNode[tokenId]
                prev = old.prev
                prev.next = old.next
                old.next.prev = prev
                new = TokenNode(tokenId, currentTime)
                prev = self.right.prev
                prev.next = new
                self.right.prev = new
                new.prev = prev
                new.next = self.right
                self.tokenToNode[tokenId] = new

    def countUnexpiredTokens(self, currentTime: int) -> int:
        curr = self.left.next
        while curr != self.right and (currentTime - curr.currentTime) >= self.timeToLive:
            self.left.next = curr.next
            curr.next.prev = self.left
            self.length -= 1
            del self.tokenToNode[curr.tokenId]
            curr = curr.next
        return self.length
    
    # TTL = 13
    # tokens = []



# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)