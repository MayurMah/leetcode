# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if(root==None):
            return False
        if(root.left==None and root.right==None):
            return (sum-root.val==0)
        left_sum_found = self.hasPathSum(root.left,sum-root.val)
        if(left_sum_found):
            return True
        right_sum_found = self.hasPathSum(root.right,sum-root.val)
        if(right_sum_found):
            return True
        return False