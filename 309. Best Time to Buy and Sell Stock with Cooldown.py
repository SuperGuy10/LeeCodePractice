'''
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times)
with the following restrictions:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:
Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]

StateA(hold): hold stock, able to sell
StateB(sell): just sold, rest only
StateC(rest): after sold, can buy stock

hold -----do nothing-----> hold: hold[i] = hold[i-1]
hold -----  to sell -----> rest: sell[i] = hold[i-1] + price[i]
rest -----do nothing-----> rest: rest[i] = rest[i-1]
rest -----  to buy  -----> hold: hold[i] = rest[i-1] - price[i]
sell -----take a rest----> rest: rest[i] = sell[i-1] 
                                                   
initial:
hold = -price[i]
sell = float("-inf")
rest = 0                                               
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        hold = -prices[0]
        sell = float("-inf")
        rest = 0
        
        for i in range(1,len(prices)):
            last_sell = sell
            hold = max(hold, rest-prices[i])
            sell = prices[i]+hold
            rest = max(rest, last_sell)
            
        return max(sell, rest)
        
        
#solution 2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2: return 0
        
        s0 = [0] * len(prices)
        s1 = [0] * len(prices) 
        s2 = [0] * len(prices) 
        
        s1[0] = -prices[0]
        
        for i in range(1, len(prices)):
            s0[i] = max(s0[i-1], s2[i-1])
            s1[i] = max(s1[i-1], s0[i-1] - prices[i])
            s2[i] = max(s2[i-1], s1[i-1] + prices[i])
            
        return max(s2[-1], s0[-1])
