##
#
# filename: max_profit.py
# by: Abhay Gupta
# date: 04-04-2020
#
# desc: given an array of prices per day, return max profit if you are able to buy and sell once
##

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        total = 0
        
        for i in range(len(prices)):
            start = i
            for j in range(i+1, len(prices)):
                end = j
                temp = prices[end] - prices[start] 
                if temp > total:
                    total = temp
        
        return total