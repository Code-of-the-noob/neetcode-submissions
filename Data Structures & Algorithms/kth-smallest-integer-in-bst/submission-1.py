# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find_nth_smallest(self,root, target) -> tuple[int,int]:
        seen_left=0
        seen_right=0        
        if root.left: 
            seen_left, res = self.find_nth_smallest(root.left,target)
            if seen_left==target:
                return target, res
        
        if target-seen_left==1:
            return 1, root.val

        if root.right:
            r_target=target-1-seen_left
            seen_right, res=self.find_nth_smallest(root.right,r_target)
            if seen_right==r_target:
                return target, res

        return seen_left+seen_right+1, None


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        _, res=self.find_nth_smallest(root,k)
        return res
        