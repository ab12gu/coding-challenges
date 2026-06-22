class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        length = len(nums) 
        stack = [[nums[0]]]

        for i in range(1,length):
            stack.append([nums[i]])
            for j in stack:
                if j[-1] < nums[i]:
                    stack.append(j + [nums[i]])

        longest = 1
        for i in stack:
            if len(i) > longest:
                longest = len(i)

        return longest

