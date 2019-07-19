'''
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; 
and a non-negative integer fee representing a transaction fee.
You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. 
You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)
Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Note:
0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
'''

# Greedy solution. Too slow
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n<2:
            return 0
        res = 0
        mini = prices[0]
        for i in range(1,n):
            if prices[i]<mini:
                mini = prices[i]
            if prices[i]>mini+fee:
                res += prices[i]-mini-fee
                mini = prices[i]-fee
        return res

# DP Solution
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) < 2:
            return 0
        earn = 0
        hold = -prices[0]
        
        for i in range(1,len(prices)):
            earn = max(earn, hold+prices[i]-fee)
            hold = max(hold, earn-prices[i])
        return earn
        
'''
Only 1 share of the stock can be bought or sold;
A stock can be bought or sold for multiple times in one day, but it has to be sold before being bought again;
The service fee is only charged when stock is sold;
Cash(i): the cash in hand, if you are not holding the stock at the end of day(i):
You might be not holding the stock at the end of day(i-1), and do nothing in day(i): a = cash(i-1); or
You might be holding the stock at the end of day(i-1), and sell it at the end of day(i):
b = hold(i-1) + prices[i] - fee;
Choose the greatest one as the value of cash(i) to get the greater potential profit:
cash(i) = max(a, b) = max(cash(i-1), hold(i-1) + prices[i] - fee);
Hold(i): the cash in hand, if you are holding the stock at the end of day(i):
You might be holding the stock at the end of day(i-1), and do nothing in day(i): a = hold(i-1); or
You might be not holding the stock at the end of day(i-1), and buy it at the end of day(i): b = cash(i-1) - prices[i]; or
You might be holding the stock at the end of day(i-1), sell it on day(i), and buy it again at the end of day(i):
c = (hold(i-1) + prices[i] - fee) - prices[i];
Choose the greatest one as the value of hold(i) to get the greater potential profit:
hold(i) = max(a,b,c)
Because max(b, c) = max(cash(i-1), hold(i-1) + prices[i] - fee) - prices[i] = cash(i) - prices[i],
so hold(i) = max(hold(i-1), cash(i) - prices[i]);
There is another way to calculate hold(i), which is more straight forward:
You might be holding the stock at the end of day(i-1), and do nothing in day(i): a = hold(i-1); or
You might be not holding the stock at the end of day(i-1), and buy it at the end of day(i): b = cash(i-1) - prices[i]; or
You might be holding the stock at the end of day(i-1), sell it on day(i), and buy it again at the end of day(i):
c = (hold(i-1) + prices[i] - fee) - prices[i] = hold(i-1) - fee;
Obviously, a > c, so max(a, c) = a, hold(i) = max(a, b, c) = max(a, b) = max(hold(i-1), cash(i-1) - prices[i])
The target is to find the maximum profit at the end of day(N): cash(N);

Check out
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/most-consistent-ways-of-dealing-with-the-series-of-stock-problems
'''
