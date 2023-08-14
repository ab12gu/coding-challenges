# filename: 215-kth-largest-element-in-an-array
# by: Abhay Gupta
# date: 23-08-14



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      # nums.sort(reverse=True)
      # return nums[k-1]

      low = min(nums)
      high = max(nums)
      occurance_array = [0 for i in range(low,  high+1)]

      for i in nums:
        occurance_array[i-low] += 1

      curr = 0

      for i in range(len(occurance_array)-1,-1, -1):
        curr += occurance_array[i]
        if curr >= k:
          return i + low


      
