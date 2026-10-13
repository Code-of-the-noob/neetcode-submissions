# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def check_equivalance(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        
        if node1 is None or node2 is None or node1.val!=node2.val:
            return False

        return self.check_equivalance(node1.left,node2.left) and \
        self.check_equivalance(node1.right,node2.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None or (root is None and subRoot is None):
            return True

        if root is None:
            return False

        stack=[root]
        while stack:
            node=stack.pop()
            if node.val == subRoot.val:
                if self.check_equivalance(node, subRoot):
                    return True
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        return False

        