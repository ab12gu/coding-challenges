# Idk

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        new_array = [0] * len(nums)
        sorted_nums = sorted(nums)
        pivot_index = -1

        for c, i in enumerate(sorted_nums):
            if i == pivot:
                pivot_index = c + 1
                new_array[c] = pivot
                continue
            if i > pivot and pivot_index == -1:
                pivot_index = c
                break

        less = 0
        greater = pivot_index
        flag = 0
        for c, i in enumerate(nums):
            if i == pivot:
                continue
            if i < pivot:
                new_array[less] = i
                less += 1
            elif i > pivot:
                new_array[greater] = i
                greater += 1
        
        return new_array
