class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        merged = nums1[:m] + nums2
        merged.sort()
        nums1[:] = merged
        
