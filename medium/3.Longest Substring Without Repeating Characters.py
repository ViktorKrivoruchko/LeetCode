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

# эффективное решение - O(n). Через хеш-таблицу и скользящее окно
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = result = 0
        for right, symbol in enumerate(s):
            if symbol in last_seen and last_seen[symbol] >= left:
                left = last_seen[symbol] + 1
            last_seen[symbol] = right
            result = max(result, right - left + 1)
        return result