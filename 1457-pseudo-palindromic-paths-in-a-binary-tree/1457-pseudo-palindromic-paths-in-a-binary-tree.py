# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        dic = [0] * 10
        def dfs(node, i):
            nonlocal dic
            if not node:
                return 0
            if not node.left and not node.right:
                dic[node.val] += 1
                odd = 0
                for val in dic:
                    if val % 2 == 1:
                        odd += 1
                dic[node.val] -= 1
                if (odd == 1 and i % 2 == 1) or not odd:
                    return 1
                else:
                    return 0
            res = 0
            dic[node.val] += 1
            res += dfs(node.left, i + 1)
            res += dfs(node.right, i + 1)
            dic[node.val] -= 1
            return res
        
        return int(dfs(root, 1))
            

