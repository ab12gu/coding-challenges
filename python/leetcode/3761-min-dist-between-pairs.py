class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        numsR = []
        for num in nums:
            temp = ""
            num = [int(x) for x in str(num)]
            for i in range(len(num)):
                temp = temp + str(num[-i-1])
            numsR.append(int(temp))

        length = len(nums) 
        output = []
        for j in range(length):
            for i in range(j+1, length):
                if numsR[j] == nums[i]:
                    output.append(abs(j-i))

        if not output:
            return -1
        return min(list(filter(lambda x: x > 0, output)))



       
