class Solution:
    def MedianOfTwo(nums1, nums2):
        num = nums1 + nums2
        num.sort()
        if (len(num) % 2) == 0:
            return((num[len(num) // 2 - 1] + num[len(num) // 2]) / 2)
        else:
            return(num[len(num) // 2])
Solution.MedianOfTwo([1, 3, 5], [5, 6, 2])