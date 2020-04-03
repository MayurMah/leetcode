# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        #print(root)
        if(root==None):
            return 0
        else:
            left_depth = self.minDepth(root.left)
            right_depth = self.minDepth(root.right)
            if(left_depth==0 or right_depth==0):
                return 1+left_depth+right_depth
            return 1+min(left_depth,right_depth)