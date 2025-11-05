class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        finishWord = ""
        strs=sorted(strs)
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if (strs[0][i] != strs[-1][i]):
                return finishWord
            finishWord += strs[0][i]
            i += 1
        return finishWord