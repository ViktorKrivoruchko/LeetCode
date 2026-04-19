# нативное решение. По времени O(n), по памяти O(n)
class Solution1:
    def myAtoi(self, s: str) -> int:
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        result = ""
        s = s.strip()
        if s and (s[0] == "+" or s[0] == "-"):
            result += s[0]
            s = s[1:]
        for i in s:
            if i in nums:
                result += i
            else:
                if result and (result.isdigit() or result[1:].isdigit()):
                    result = int(result)
                    if result < -2147483648:
                        return -2147483648
                    elif result > 2147483647:
                        return 2147483647
                    else:
                        return result
                else:
                    return 0
        if result and (result.isdigit() or result[1:].isdigit()):
            result = int(result)
            if result < -2147483648:
                return -2147483648
            elif result > 2147483647:
                return 2147483647
            else:
                return result
        else:
            return 0

# улучшенное решение. Время O(n), память O(n)
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        s = s.strip()
        if not s:
            return 0

        sign = -1 if s[0] == "-" else 1
        s = s[1:] if s[0] in "+-" else s

        result = 0
        for c in s:
            if not c.isdigit():
                break
            result = result * 10 + int(c)

        return max(INT_MIN, min(INT_MAX, sign * result))