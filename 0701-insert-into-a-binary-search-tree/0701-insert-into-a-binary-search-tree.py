# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def dfs(curr):
            if val < curr.val and not curr.left:
                curr.left = TreeNode(val)
                return
            
            if val > curr.val and not curr.right:
                curr.right = TreeNode(val)
                return
            
            if val < curr.val:
                dfs(curr.left)
                return
            
            if val > curr.val:
                dfs(curr.right)
                return
        
        dfs(root)
        return root
