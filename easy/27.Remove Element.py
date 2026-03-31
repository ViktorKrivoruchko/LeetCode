# нативное решение
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
    
# решение через два указателя
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in nums:
            if fast != val:
                nums[slow] = fast
                slow += 1
        return slow

# используя встроенные функии
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = filter(lambda x: x != val, nums)
        return len(nums)