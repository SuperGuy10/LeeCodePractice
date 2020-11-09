'''
Today, the bookstore owner has a store open for customers.length minutes.  
Every minute, some number of customers (customers[i]) enter the store, 
and all those customers leave after the end of that minute.
On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, 
otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, 
otherwise they are satisfied
The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.
Return the maximum number of customers that can be satisfied throughout the day.

Example 1:
Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
 
Note:
1 <= X <= customers.length == grumpy.length <= 20000
0 <= customers[i] <= 1000
0 <= grumpy[i] <= 1
'''

# TLE
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        res = 0
        total = 0
        for i in range(len(grumpy)-X+1):
            #print(grumpy)
            tem = grumpy[:] #assign one list equal to another: use list() or list[:]
            tem[i:i+X] = [0]*X
            #print(tem)
            for j in range(len(customers)):
                if tem[j] == 0:
                    total += customers[j]
            if total > res:
                res = total
            total = 0
        return res
   
   #solution 3
   class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        happy_sum = 0
        max_sub = 0
        grumpy_sum = 0
        for i in range(len(customers)):
            if not grumpy[i]:
                happy_sum += customers[i]
            if i >= X:
                if grumpy[i - X]:
                    grumpy_sum -= customers[i - X]
            if grumpy[i]:
                grumpy_sum += customers[i]
                max_sub = max(grumpy_sum, max_sub)
        return happy_sum + max_sub
'''
Window Sliding Problem
Tow parts: first to calculate the sum of all satisfied customer. Then to calculate the max satisfied customer in X
Add them together
'''

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        res = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                res += customers[i]
                customers[i] = 0 #change then to 0 so no need for us to find out we need to subtract or not.

        total = 0
        max_count = 0
        for j in range(len(customers)):
            if j < X:
                total += customers[j]
                continue
            max_count = max(total, max_count)
            total -= customers[j-X]
            total += customers[j]
            #print(max_count)
        max_count = max(total, max_count) #to check the last round
        #print("final",max_count)
        return res+max_count
