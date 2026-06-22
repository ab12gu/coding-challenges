class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums.reverse()

        curr = nums.pop()
        return self.longest(curr, nums)

    def longest(self, curr, nums):
        new = nums.pop()
        count = 1

        if new > curr:
            count += self.longest(new, nums)
        
        return count
