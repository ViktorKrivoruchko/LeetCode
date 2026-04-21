# нативное решение. Время O(n*m*logn), память O(n)
class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        strs=sorted(strs)
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if (strs[0][i] != strs[-1][i]):
                return result
            result += strs[0][i]
        return result

# время O(n*m), память O(n)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]
        for word in strs:
            for s in range(min(len(word), len(result))):
                if word[s] != result[s]:
                    result = result[:s]
                    break
            result = result[:min(len(word), len(result))]
        return result

# решение через zip(). время O(n*m), память O(n)
class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                result += chars[0]
            else:
                break
        return result