# 88 Merge Sorted Array

class Solution:
    def __init__(self):
        pass
    def merge(self, nums1, m, nums2, n):

        nums1[m:] = nums2
        nums1.sort()
        print(nums1)

if __name__ == "__main__":
    class_instance = Solution()

    class_instance.merge([1,2], 2, [1, 3], 4)


