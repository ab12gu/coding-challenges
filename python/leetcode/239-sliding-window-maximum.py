# filename: 235-sliding-window-maximum.py
# by: Abhay Gupta
# date: 23-08-15

# First Solution
# Un-optimized

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
      i = 0
      total = len(nums)
      output = []

      for i in range(total - k + 1):
        window = []
        for j in range(k):
          window.append(nums[i+j])
        output.append(max(window))

      return output


 # Second Solution

class Solution:
  def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    import bisect

    i = 0
    total = len(nums)
    output = []

    window = sorted(nums[0:k])
    output.append(window[-1])

    for i in range(k, total):
      window.remove(nums[i - k])
      bisect.insort(window, nums[i])
      output.append(window[-1])

    return output

# Third Solution

  class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
      import bisect

      i = 0
      total = len(nums)
      output = []

      window = sorted(nums[0:k])
      output.append(window[-1])

      for i in range(k, total):
        j = bisect.bisect(window, nums[i - k])
        del (window[j - 1])
        bisect.insort(window, nums[i])
        output.append(window[-1])

      return output

