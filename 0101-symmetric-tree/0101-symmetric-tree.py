# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def swap(node):
            if not node:
                return

            swap(node.left)
            swap(node.right)
            tmp = node.left
            node.left = node.right
            node.right = tmp

        swap(root.right)

        q = deque([[root.left, root.right]])

        while q:
            qLen = len(q)

            for _ in range(len(q)):
                left_node, right_node = q.popleft()

                if not left_node and not right_node:
                    continue

                if (left_node and not right_node) or (not left_node and right_node):
                    return False

                if left_node.val != right_node.val:
                    return False
            
                q.append([left_node.left, right_node.left])
                q.append([left_node.right, right_node.right])
            
        return True
            
            

