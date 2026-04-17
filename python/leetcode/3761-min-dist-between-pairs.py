class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:

        numsR = []
        table = {}

        for c, num in enumerate(nums):

            num = [x for x in str(num)]
            num.reverse()
            num = int("".join(num))

            if num in table:
                table[num].append(c)
            else:
                table[num] = [c]

        output = -1

        for j, num in enumerate(nums):    
            if num in table:
                for i in table[num]:
                    if i < j:
                        dist = abs(j-i)
                        if output == -1 or dist < output:
                            output = dist
                            continue
                        if output > -1 and dist > output:
                            break
        return output
