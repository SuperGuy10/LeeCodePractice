'''
Tag: Array; Difficulty: Easy.
Given an index k, return the kth row of the Pascal's triangle.
For example, given k = 3,
Return [1,3,3,1].
Note:
Could you optimize your algorithm to use only O(k) extra space?
'''

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rt=[1]*(rowIndex+1)
        for i in range(2, rowIndex+1):
            for j in range(1, i):
                rt[i-j]+=rt[i-j-1]
        return rt
        
        
'''
Smart solution:
combine map() and lambda() to twist sum each new row.
eg:"[0]+res, res+[0]" means
 0 1 2 1
+1 2 1 0
------------
 1 3 3 1
'''
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(rowIndex):
            res = list(map(lambda x, y: x+y, [0]+res, res+[0]))
        return res
