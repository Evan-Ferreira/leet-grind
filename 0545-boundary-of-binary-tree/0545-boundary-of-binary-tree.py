# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        self.res = [root.val]

        def getLeftBoundary(node):
            ans = []
            while node:
                if node.left or node.right:
                    ans.append(node.val)
                if node.left:
                    node = node.left
                else:
                    node = node.right
            return ans
        
        def getRightBoundary(node):
            ans = []
            while node:
                if node.left or node.right:
                    ans.append(node.val)
                if node.right:
                    node = node.right
                else:
                    node = node.left
            ans.reverse()
            return ans
        
        def getLeaves(node):
            if not node:
                return
            if not node.left and not node.right:
                self.res.append(node.val)
                return

            getLeaves(node.left)
            getLeaves(node.right)
        
        self.res += getLeftBoundary(root.left)
        if root.left or root.right:
            getLeaves(root)
        self.res += getRightBoundary(root.right)
        return self.res