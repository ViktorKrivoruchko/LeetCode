'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.

Return k.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

from typing import List


# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         nums.remove(val)
#         return len(nums)
        
# s1 = Solution([3,2,2,3], 3)
# print(s1.removeElement())

class Solution:
    def __init__(self, nums: List[int], val: int):
        self.nums = nums
        self.val = val
        
    def removeElement(self) -> int:
        while self.val in self.nums:
            self.nums.remove(self.val)
        return len(self.nums)
    
s1 = Solution([3,2,2,3], 3)
print(s1.removeElement())