class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    d = collections.defaultdict(int)

    for i in nums:
      d[i] += 1

    freq = [[] for i in range(len(nums)+1)]
    
    for i in d:
      freq[d[i]].append(i)

    count = 0 
    output = []
    for i in range(len(nums)):
      for j in freq[-(1+i)]:
        output.append(j)

        if k == (count := count + 1):
          return output
        



