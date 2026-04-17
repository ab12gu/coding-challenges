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

# Alternate solution, but didn't work with edge case, too slow

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:

        numsR = []
        table = {}
        initial = {}
        reciprical = {}

        for c, num in enumerate(nums):
            orig = num

            num = [x for x in str(num)]
            num.reverse()
            num = int("".join(num))

            if num in table:
                table[num].append(c)
            else:
                table[num] = [c]

            if orig in initial:
                if num in reciprical:
                    reciprical[num].extend([c, initial[orig]])
                else:
                    reciprical[num] = [c, initial[orig]]
            else:
                initial[num] = c

        output = -1

        #print("R",reciprical)
        print("T",table)

        for i in reciprical:
            diff = [abs(x - y) for x in reciprical[i] for y in table[i] ]
            dist = min(filter(lambda x: x > 0, diff))
            if dist > 0 and (output == -1 or dist < output):
                output = dist
        return output

