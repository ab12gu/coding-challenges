class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:

    # implement linear hashmap
    size = len(nums)
    if size == 1:
      return False

    high = max(nums) + 1
    duplicates = [high] * size

    for i in nums:
      index = i % size

      while(1):
        if duplicates[index] == i:
          print(index, i)
          return True
        elif duplicates[index] == high:
          duplicates[index] = i
          break
        index = (index + 1) % size

    return False

    # simple hashmap solution

    bucket = {}
    for i in nums:
      if i not in bucket:
        bucket[i] = i
      else:
        return True
    return False





