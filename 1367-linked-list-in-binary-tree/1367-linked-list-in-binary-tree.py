# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def dfsCheck(treeNode, listNode):
            if not listNode:
                return True
            if not treeNode:
                return False
            
            if treeNode.val == listNode.val:
                listNode = listNode.next
            else:
                return False
            
            return dfsCheck(treeNode.left, listNode) or dfsCheck(treeNode.right, listNode)
        
        def dfs(treeNode):
            if not treeNode:
                return False
            
            if treeNode.val == head.val:
                if dfsCheck(treeNode, head): 
                    return True

            return dfs(treeNode.left) or dfs(treeNode.right)
        return dfs(root)


