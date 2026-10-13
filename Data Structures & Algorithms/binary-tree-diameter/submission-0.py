# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def calc_diameter(self, node) -> (int, int):
        if node is None:
            return 0,0

        left_dia, left_depth = self.calc_diameter(node.left)
        right_dia, right_depth = self.calc_diameter(node.right)


        max_depth= 1+ max(left_depth,right_depth)
        dia_node = 1+ left_depth + right_depth
        sub_tree_max_dia=max(left_dia,right_dia,dia_node)

        return sub_tree_max_dia, max_depth

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans,_ = self.calc_diameter(root)
        return ans-1

        