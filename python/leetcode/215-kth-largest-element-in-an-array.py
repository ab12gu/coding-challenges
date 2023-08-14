# filename: 215-kth-largest-element-in-an-array
# by: Abhay Gupta
# date: 23-08-14

# class definition
class Solution:

    # main method / no constructor
    def findKthLargest(self, nums: List[int], k: int) -> int:
      
      # intialize variables
      low = min(nums)
      high = max(nums)
      occurance_array = [0 for i in range(low,  high+1)]

      # count occurances per element in array
      for i in nums:
        occurance_array[i-low] += 1

      # reverse through occurances array and return the kth largest value
      curr = 0
      for i in range(len(occurance_array)-1,-1, -1):
        curr += occurance_array[i]
        if curr >= k:
          return i + low


      
