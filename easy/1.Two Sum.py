from typing import List


class Solution:
    # нативное решение O(n^2)
    def twoSumNative(self, nums: List[int], target: int) -> List[int]:
        for f_index, f_num in enumerate(nums):
            for s_index, s_num in enumerate(nums[f_index+1:]):
                if f_num + s_num == target:
                    return [f_index, s_index+f_index+1]
    
    # оптимальное решение через хеш-таблицу: O(n) по времени и памяти
    def twoSumHashTable(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, n in enumerate(nums):
            if target-n in num_dict:
                return [num_dict[target-n], i]
            num_dict[n] = i