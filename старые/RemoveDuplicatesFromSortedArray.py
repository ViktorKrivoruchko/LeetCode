class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        meanerList = []
        for symbol in nums:
            if symbol not in meanerList:
                meanerList += symbol
            else:
                meanerList += "_"
        return meanerList
    
Solve = Solution()
Solve.removeDuplicates([0,0,1,1,1,1,2,3,3])