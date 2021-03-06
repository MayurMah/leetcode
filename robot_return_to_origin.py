class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """Refer https://leetcode.com/problems/robot-return-to-origin/ for problem description"""

        U = moves.count("U")
        D = -1 * moves.count("D")
        L = moves.count("L")
        R = -1 * moves.count("R")
        if U + D == 0 and L + R == 0:
            return True
        else:
            return False
