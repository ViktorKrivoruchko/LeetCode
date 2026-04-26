# решение через рекурсию O(2^n)
class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        if p == "" and s == "":
            return True
        elif p == "":
            return False
        elif s == "" and (len(p) < 2 or p[1] != "*"):
            return False
        elif len(p) >= 2 and p[1] == "*":
            if s == "":
                return self.isMatch(s, p[2:])
            if p[0] != s[0] and p[0] != ".":
                return self.isMatch(s, p[2:])
            else:
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
        elif s[0] == p[0] or p[0] == ".":
            return self.isMatch(s[1:], p[1:])
        else:
            return False