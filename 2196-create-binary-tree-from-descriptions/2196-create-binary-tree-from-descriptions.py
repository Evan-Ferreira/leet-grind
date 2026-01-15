# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        m = defaultdict(lambda: [None, None])
        children = set()
        parents = set()

        for par, child, isLeft in descriptions:
            if not isLeft:
                m[par][1] = child
            else:
                m[par][0] = child
            children.add(child)
            parents.add(par)
        
        root = (parents - children).pop()

        def dfs(curr):
            if not curr:
                return None
            node = TreeNode(curr)
            node.left = dfs(m[curr][0])
            node.right = dfs(m[curr][1])
            return node
        
        return dfs(root)



        
