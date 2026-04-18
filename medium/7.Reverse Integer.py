# Эффективность O(n)
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            result = int(str(x)[::-1])
        elif x < 0:
            x *= -1
            result = int(str(x)[::-1]) * -1
        if result < -2147483648 or result > 2147483647:
            return 0
        return int(result)