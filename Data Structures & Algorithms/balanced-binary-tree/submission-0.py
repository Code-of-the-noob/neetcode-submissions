# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check_heights(self,node):
        if node is None:
            return 0, True
        
        lh,lb = self.check_heights(node.left)
        rh,rb = self.check_heights(node.right)
        return 1+max(lh,rh), rb and lb and abs(lh-rh)<=1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, ans = self.check_heights(root)
        return ans