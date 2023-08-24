class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

      nums_set = set(nums)

      if not nums:
        return 0

      longest = 1
      for i in nums:
        curr = 1
        j = i
        while(1):
          if j + 1 in nums_set:
            curr += 1
            j += 1
            nums_set.remove(j)
          else:
            break
        j = i
        while(1):
          if j - 1 in nums_set:
            curr += 1
            j -= 1
            nums_set.remove(j)
          else:
            break
        
        if curr > longest:
          longest = curr
      
      return longes
