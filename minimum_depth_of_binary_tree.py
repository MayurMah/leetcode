# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """Given a binary tree, find its minimum depth.
        The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

        Args:
            root: root node

        Returns:
            Minimum depth (int)

        """

        if root is None:
            return 0
        else:
            left_depth = self.minDepth(root.left)
            right_depth = self.minDepth(root.right)
            if left_depth == 0 or right_depth == 0:
                return 1 + left_depth + right_depth
            return 1 + min(left_depth, right_depth)
