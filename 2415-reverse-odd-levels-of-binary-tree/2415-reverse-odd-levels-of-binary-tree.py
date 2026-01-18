# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        q = collections.deque()
        q.append(root)
        curr = 0
        while q:
            qLen = len(q)
            level = []
            if curr % 2 == 1:
                for i in range(qLen):
                    level.append(q[i].val)

            for j in range(qLen - 1, -1, -1):
                node = q.popleft()
                if curr % 2 == 1:
                    node.val = level[j]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            curr += 1
        return root

