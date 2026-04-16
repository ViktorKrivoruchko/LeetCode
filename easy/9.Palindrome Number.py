# нативное решение. O(n) по времени и по памяти
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        i = str(x)
        left, right = 0, len(i) -1
        while left < right:
            if i[left] == i[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

# более короткое решение через сравнение среза с такой же эффективностью
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if x < 0:
            return False
        return s == s[::-1]