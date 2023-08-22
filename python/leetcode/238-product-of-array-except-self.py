class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
      
      right = 1
      left = 1
      right_list = [1]
      left_list = [1]

      for c in range(len(nums)-1):
        right *= nums[c]
        right_list.append(right)
        left *= nums[-(1+c)]
        left_list.append(left)

      print(right_list)
      print(left_list)
      answer = []
      for c in range(len(nums)):
        answer.append(right_list[c]*left_list[-(c+1)])

      return(answer
