class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:

        numsR = []
        for num in nums:
            
            num = [x for x in str(num)]
            num.reverse()
            numsR.append(int("".join(num)))

        length = len(nums) 
        output = length

        for j in range(length):
            for i in range(j+1, min(j + output, length)):
                if numsR[j] == nums[i]:
                    dist = abs(j-i)
                    if dist < output:
                        output = dist

        if output == length:
            return -1
        return output
