# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue=[]
        queue.append((p,q))

        for i,j in queue:
            if i is None and j is None:
                continue
            
            if i is None or j is None:
                return False

            if i.val!=j.val:
                return False
                
            queue.append((i.left,j.left))
            queue.append((i.right,j.right))


        return True