# нативное решение за O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = right = 0
        min_l = max_r = 0
        for center in range(len(s)):
            left, right = center - 1, center + 1
            while left >= 0 and right <= (len(s) - 1) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left > max_r - min_l:
                min_l, max_r = left, right
            left, right = center, center + 1
            
            while left >= 0 and right <= (len(s) - 1) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left > max_r - min_l:
                min_l, max_r = left, right
        return s[min_l+1:max_r]

# TODO: решить алгоритмом Манакера