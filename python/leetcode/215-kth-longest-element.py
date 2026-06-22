class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [nums[0]]

        for i in range(1,len(nums)):
            flag = False
            for j in range(len(heap)):

                print(i,j, heap)
                if nums[i] >= heap[j]:
                    heap = heap[:j] + [nums[i]] + heap[j:]
                    flag = True
                    break
            if flag == False:
                heap.append(nums[i])
        print(heap)
        return heap[k-1]
