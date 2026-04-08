# нативное решение. Эффективность O(n^2)
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = ""
        check = ""
        for symbol in s:
            if symbol in check and len(check) > len(result):
                result = check
                check = check[check.index(symbol)+1:]
                check += symbol
            elif symbol in check and len(check) <= len(result):
                check = check[check.index(symbol)+1:]
                check += symbol
            else:
                check += symbol
        if len(result) < len(check):
            result = check
        return len(result)