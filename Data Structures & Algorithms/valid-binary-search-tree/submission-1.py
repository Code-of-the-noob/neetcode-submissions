# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check_validity(self, node) -> (bool,int, int):
        left_min, left_max, right_min, right_max= node.val,node.val,node.val,node.val
        if node.left:
            left_valid,left_min, left_max= self.check_validity(node.left)
            if not left_valid or left_max>=node.val:
                return False, 0, 0

        if node.right:
            right_valid,right_min, right_max= self.check_validity(node.right)
            if not right_valid or right_min<=node.val:
                return False,0,0

        return True, left_min, right_max


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True

        result,_,_= self.check_validity(root)
        return result
        