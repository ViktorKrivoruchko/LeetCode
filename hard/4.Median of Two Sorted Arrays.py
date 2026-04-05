from typing import List


# нативное решение. O((n+m) log(n+m)) и O(n+m) по памяти
class Solution1:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
        else:
            return nums[len(nums) // 2]

# более эффективно можно решить бинарным поиском
# TODO: решить бинарным поиском
