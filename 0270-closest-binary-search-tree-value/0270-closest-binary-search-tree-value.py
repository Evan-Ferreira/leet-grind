# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = float('inf')
        def search(node, prev):
            nonlocal res
            if not node:
                if (abs(prev.val - target) < abs(res - target) or 
                    abs(prev.val - target) == abs(res - target) and prev.val < res):
                    res = prev.val
                return

            elif node.val == target:
                res = node.val

            elif node.val < target and target < prev.val or node.val > target and prev.val < target:
                if (abs(node.val - target) >= abs(prev.val - target) and 
                    (abs(prev.val - target) < abs(res - target) or 
                    abs(prev.val - target) == abs(res - target) and prev.val < res)):
                    res = prev.val
                elif (abs(node.val - target) <= abs(res - target) or 
                    abs(node.val - target) == abs(res - target) and node.val < res):
                    res = node.val
            
            if target > node.val:
                search(node.right, node)
            else:
                search(node.left, node)
        
        search(root, root)
        return res