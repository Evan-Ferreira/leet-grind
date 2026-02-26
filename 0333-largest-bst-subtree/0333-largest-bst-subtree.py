# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node):
            if not node:
                return [float('inf'), float('-inf'), 0]
            
            minLeft, maxLeft, leftSize = dfs(node.left)
            minRight, maxRight, rightSize = dfs(node.right)

            if not (node.val > maxLeft and node.val < minRight):
                return [float('-inf'), float('inf'), max(leftSize, rightSize)]
            minVal = max(maxLeft, maxRight, node.val)
            maxVal = min(minLeft, minRight, node.val)
            return [maxVal, minVal, leftSize + rightSize + 1]
        return dfs(root)[2]
            