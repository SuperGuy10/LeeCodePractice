'''
Tag: Array; Difficulty: Easy.
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5
max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0
In this case, no transaction is done, i.e. max profit = 0.
'''

'''
For this question itself, it's not difficult but I midunderstand it twice. Understanding the question is really important.
'''
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0 
        
        min = prices[0]
        max_Profit = 0
        for price in prices:
            if price < min:
                min = price
            if price-min > max_Profit:
                max_Profit = price-min
        return max_Profit

'''
For the second solution is the fasted one. Pay attentation on folat("inf"), which means infinite.
'''
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxSoFar = 0
        minSoFar = float("inf")
        for num in prices:
            if num < minSoFar:
                minSoFar = num
            elif num - minSoFar > maxSoFar:
                maxSoFar = num - minSoFar
        return maxSoFar
