class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:

    bucket = {}
    for i in nums:
      if i not in bucket:
        bucket[i] = i
      else:
        return True
    return False





