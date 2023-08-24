class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      
      hashtable = {}
      for c, i in enumerate(numbers):
        if hashtable.get(target - i) != None:
          return [hashtable[target - i] + 1, c + 1]
        else:
          hashtable[i] = 
