class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        output = set()

        for i in nums:
            if i in output:
                output.remove(i)
            else:
                output.add(i)

        if output:
            return False
        return True

        #[output.remove(i) if i in output else output.add(i) for i in nums]
