 class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        q_len = len(queries)
        output = [-1] * q_len
        high = len(nums)

        sorted_nums = sorted(enumerate(nums), key = lambda x: x[1])
        sorted_nums_dict = {}

        for i in sorted_nums:
            if i[1] in sorted_nums_dict:
                sorted_nums_dict[i[1]].append(i[0])
            else:
                sorted_nums_dict[i[1]] = [i[0]]

        for c, q in enumerate(queries):
            if nums[q] in sorted_nums_dict:
                data = []
                for x in sorted_nums_dict[nums[q]]:
                    y = abs(q-x)
                    data.extend( (y, abs(high-y)) )
                if data[0] != 0 or len(data) > 2:
                    output[c] = min(filter(lambda x: x != 0, data))

        return output
"""
        for i in range(q_len):
            index = queries[i]
            num = nums[index]

            for j in range(high):
                if index != j:
                    if nums[j] == num:
                        dist = abs(index-j)
                        low = min(high - dist, dist)
                        if low < output[i] or output[i] == -1:
                            output[i] = low
        return output
 """       

              
