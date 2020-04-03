# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the
        values along the path equals the given sum.

        Args:
            root: root code of the binary tree
            sum: target sum

        Returns:
            True if the tree has path from root to leaf that sums to target sum, otherwise False.

        """
        if root is None:
            return False
        if root.left is None and root.right is None:
            return sum - root.val == 0
        left_sum_found = self.hasPathSum(root.left, sum - root.val)
        if left_sum_found:
            return True
        right_sum_found = self.hasPathSum(root.right, sum - root.val)
        if right_sum_found:
            return True
        return False
