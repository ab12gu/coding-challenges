class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        q_len = len(queries)
        output = [-1] * q_len
        high = len(nums)

        for i in range(q_len):
            index = queries[i]

            for j in range(high):
                if index != j:
                    if nums[j] == nums[index]:
                        dist = abs(index-j)
                        low = min(high - dist, dist)
                        if low < output[i] or output[i] == -1:
                            output[i] = low
        
        return output


