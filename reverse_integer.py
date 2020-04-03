class Solution:
    def reverse(self, x: int) -> int:
        """Given a 32-bit signed integer, reverse digits of an integer.

        Args:
            x: given 32-bit signed integer

        Returns:
            Reverse of the given integer Ex. 321 for 123

        """
        upper = 2 ** 31 - 1
        lower = 2 ** 31
        x_reverse = 0

        is_negative = True if x < 0 else False
        x = abs(x)

        while x != 0:
            rem = x % 10
            x = x // 10

            if not is_negative:
                if x_reverse > upper // 10 or (x_reverse == upper and rem > 7):
                    return 0
            elif x_reverse > lower // 10 or (x_reverse == lower and rem > 8):
                return 0

            x_reverse = x_reverse * 10 + rem

        return -1 * x_reverse if is_negative else x_reverse
