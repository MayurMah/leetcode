# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getLevel(self, node):
        """Get number of levels that fall under a node in the binary tree"""

        if node is None:
            return 0
        else:
            left_level = self.getLevel(node.left)
            right_level = self.getLevel(node.right)
            if abs(left_level - right_level) >= 2 or left_level == -1 or right_level == -1:
                return -1
            else:
                return 1 + max(left_level, right_level)

    def isBalanced(self, root: TreeNode) -> bool:
        """Check if a binary tree is balanced - balanced means that the tree has same number of levels in the left and
        right branch

        Args:
            root: the root node of the binary tree

        Returns:
            True if the tree is balanced. Otherwise, return False.

        """

        if self.getLevel(root) == -1:
            return False
        else:
            return True
